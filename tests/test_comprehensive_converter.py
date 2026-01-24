#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test suite for the comprehensive converter.
Tests all features: auto-detection, temperatures, dates, years, etc.
"""

import csv
import sys

from num2words2.converters.comprehensive_converter import ComprehensiveConverter


def _run_temperature_conversion():
    converter = ComprehensiveConverter()

    test_cases = [
        ("Il fait 25°C aujourd'hui.", "fr", None),
        ("Heute sind es -10 Grad.", "de", None),
        ("La temperatura es 30 grados.", "es", None),
        ("The temperature is 72 degrees.", "en", None),
        ("Сегодня 20 градусов.", "ru", "ru"),
        ("今日の気温は28度です。", "ja", "ja"),
        ("Vandaag is het 15 graden.", "nl", "nl"),
    ]

    print("\n" + "=" * 60)
    print("TEMPERATURE CONVERSION TESTS")
    print("=" * 60)

    passed = 0
    failed = 0

    for sentence, expected_lang, force_lang in test_cases:
        result = converter.convert_sentence(sentence, force_language=force_lang)
        detected = converter.lang

        if not force_lang and detected != expected_lang:
            print(f"⚠️  Language mismatch: expected {expected_lang}, got {detected}")

        if any(char.isdigit() for char in result):
            print(f"❌ FAIL: {sentence[:40]}...")
            print(f"   Result still has digits: {result}")
            failed += 1
        else:
            print(f"✅ PASS [{detected}]: {sentence[:40]}...")
            passed += 1

    print(f"\nResults: {passed} passed, {failed} failed")
    return passed, failed


def test_temperature_conversion():
    """Test temperature conversion across languages."""
    _, failed = _run_temperature_conversion()
    assert failed == 0


def _run_date_conversion():
    converter = ComprehensiveConverter()

    test_cases = [
        ("Le 1er janvier 2025", "fr", "Le premier janvier deux mille vingt-cinq"),
        ("Am 15. Januar 2024", "de", "Am fünfzehnte Januar zweitausendvierundzwanzig"),
        ("El 3 de febrero", "es", "El tres de febrero"),
    ]

    print("\n" + "=" * 60)
    print("DATE CONVERSION TESTS")
    print("=" * 60)

    passed = 0
    failed = 0

    for sentence, lang, expected in test_cases:
        result = converter.convert_sentence(sentence, force_language=lang)

        if result.lower() == expected.lower():
            print(f"✅ PASS [{lang}]: {sentence}")
            passed += 1
        else:
            print(f"❌ FAIL [{lang}]: {sentence}")
            print(f"   Expected: {expected}")
            print(f"   Got:      {result}")
            failed += 1

    return passed, failed


def test_date_conversion():
    """Test date conversion with ordinals."""
    _, failed = _run_date_conversion()
    assert failed == 0


def run_from_csv(csv_file: str):
    """Test converter using CSV file."""
    converter = ComprehensiveConverter()

    print("\n" + "=" * 60)
    print(f"CSV TEST: {csv_file}")
    print("=" * 60)

    passed = 0
    failed = 0

    try:
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                # Handle different CSV formats
                if "language_code" in row:
                    lang = row["language_code"]
                    sentence = row["original_sentence"]
                    expected = row["full_text_conversion"]
                else:
                    lang = None  # Auto-detect
                    sentence = row.get("sentence", row.get("original", ""))
                    expected = row.get("expected", row.get("conversion", ""))

                if not sentence:
                    continue

                result = converter.convert_sentence(sentence, force_language=lang)

                # Simple comparison
                if result.strip().lower() == expected.strip().lower():
                    print(f"✅ [{lang or converter.lang}] PASS")
                    passed += 1
                else:
                    print(f"❌ [{lang or converter.lang}] FAIL")
                    print(f"   Original: {sentence[:60]}...")
                    print(f"   Expected: {expected[:60]}...")
                    print(f"   Got:      {result[:60]}...")
                    failed += 1

    except FileNotFoundError:
        print(f"❌ File not found: {csv_file}")
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")

    print(f"\nResults: {passed} passed, {failed} failed")
    return passed, failed


def _run_auto_detection():
    converter = ComprehensiveConverter()

    test_cases = [
        ("C'est une belle journée de 25 degrés.", "fr"),
        ("Das Wetter ist heute schön mit 20 Grad.", "de"),
        ("El clima está perfecto con 28 grados.", "es"),
        ("The weather is nice at 75 degrees.", "en"),
        ("Oggi fa caldo con 30 gradi.", "it"),
        ("Hoje está quente com 35 graus.", "pt"),
    ]

    print("\n" + "=" * 60)
    print("LANGUAGE AUTO-DETECTION TESTS")
    print("=" * 60)

    passed = 0
    failed = 0

    for sentence, expected_lang in test_cases:
        converter.convert_sentence(sentence)
        detected = converter.lang

        if detected == expected_lang:
            print(f"✅ Correctly detected {expected_lang}: {sentence[:40]}...")
            passed += 1
        else:
            print(f"❌ Failed detection - expected {expected_lang}, got {detected}")
            print(f"   Sentence: {sentence}")
            failed += 1

    return passed, failed


def test_auto_detection():
    """Test automatic language detection."""
    _, failed = _run_auto_detection()
    assert failed == 0


def run_all_tests():
    """Run all test suites."""
    print("\n" + "🧪" * 30)
    print("COMPREHENSIVE CONVERTER - FULL TEST SUITE")
    print("🧪" * 30)

    total_passed = 0
    total_failed = 0

    # Run each test suite
    p, f = _run_temperature_conversion()
    total_passed += p
    total_failed += f

    p, f = _run_date_conversion()
    total_passed += p
    total_failed += f

    p, f = _run_auto_detection()
    total_passed += p
    total_failed += f

    # Summary
    print("\n" + "=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)
    print(f"Total Tests: {total_passed + total_failed}")
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_failed}")

    if total_failed == 0:
        print("✅ All tests passed!")
    else:
        print(f"⚠️  {total_failed} tests failed")

    return total_failed == 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--csv" and len(sys.argv) > 2:
            run_from_csv(sys.argv[2])
        elif sys.argv[1] == "--temp":
            test_temperature_conversion()
        elif sys.argv[1] == "--date":
            test_date_conversion()
        elif sys.argv[1] == "--auto":
            test_auto_detection()
        else:
            print("Usage:")
            print("  python test_comprehensive_converter.py           # Run all tests")
            print(
                "  python test_comprehensive_converter.py --csv <file>  # Test with CSV"
            )
            print(
                "  python test_comprehensive_converter.py --temp    # Test temperatures"
            )
            print("  python test_comprehensive_converter.py --date    # Test dates")
            print(
                "  python test_comprehensive_converter.py --auto    # Test auto-detection"
            )
    else:
        run_all_tests()
