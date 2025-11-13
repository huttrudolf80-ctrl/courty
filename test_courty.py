#!/usr/bin/env python3
"""
测试文件 / Test file for courty.py
"""

import json
import os
import sys
from courty import CountryData


def test_initialization():
    """测试初始化 / Test initialization"""
    courty = CountryData()
    assert courty is not None
    print("✓ test_initialization passed")


def test_get_all_countries():
    """测试获取所有国家 / Test get all countries"""
    courty = CountryData()
    countries = courty.get_all_countries()
    assert len(countries) >= 5
    assert all('name' in c and 'code' in c for c in countries)
    print("✓ test_get_all_countries passed")


def test_get_country_by_code():
    """测试通过代码查询 / Test get country by code"""
    courty = CountryData()
    
    # Test valid code
    china = courty.get_country_by_code("CN")
    assert china is not None
    assert china['name'] == '中国'
    assert china['code'] == 'CN'
    
    # Test case insensitive
    china2 = courty.get_country_by_code("cn")
    assert china2 is not None
    
    # Test invalid code
    invalid = courty.get_country_by_code("XX")
    assert invalid is None
    
    print("✓ test_get_country_by_code passed")


def test_get_country_by_name():
    """测试通过名称查询 / Test get country by name"""
    courty = CountryData()
    
    # Test Chinese name
    us_cn = courty.get_country_by_name("美国")
    assert us_cn is not None
    assert us_cn['code'] == 'US'
    
    # Test English name
    us_en = courty.get_country_by_name("United States")
    assert us_en is not None
    assert us_en['code'] == 'US'
    
    # Test invalid name
    invalid = courty.get_country_by_name("不存在的国家")
    assert invalid is None
    
    print("✓ test_get_country_by_name passed")


def test_search_countries():
    """测试搜索国家 / Test search countries"""
    courty = CountryData()
    
    # Test search by continent
    asian = courty.search_countries(continent="亚洲")
    assert len(asian) >= 2
    assert all(c['continent'] == '亚洲' for c in asian)
    
    # Test search by continent (English)
    european = courty.search_countries(continent_en="Europe")
    assert len(european) >= 2
    assert all(c['continent_en'] == 'Europe' for c in european)
    
    # Test no results
    none_found = courty.search_countries(continent="南极洲")
    assert len(none_found) == 0
    
    print("✓ test_search_countries passed")


def test_add_country():
    """测试添加国家 / Test add country"""
    # Create a temporary test file
    test_file = "/tmp/test_countries.json"
    if os.path.exists(test_file):
        os.remove(test_file)
    
    courty = CountryData(test_file)
    
    # Add a country
    new_country = {
        "name": "德国",
        "name_en": "Germany",
        "code": "DE",
        "capital": "柏林",
        "capital_en": "Berlin"
    }
    result = courty.add_country(new_country)
    assert result == True
    
    # Verify it was added
    germany = courty.get_country_by_code("DE")
    assert germany is not None
    assert germany['name'] == '德国'
    assert 'id' in germany
    
    # Test duplicate prevention
    duplicate = courty.add_country(new_country)
    assert duplicate == False
    
    # Test missing required fields
    invalid = courty.add_country({"name": "测试"})
    assert invalid == False
    
    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)
    
    print("✓ test_add_country passed")


def test_update_country():
    """测试更新国家 / Test update country"""
    # Create a temporary test file
    test_file = "/tmp/test_countries_update.json"
    if os.path.exists(test_file):
        os.remove(test_file)
    
    courty = CountryData(test_file)
    
    # Add a country
    new_country = {
        "name": "德国",
        "name_en": "Germany",
        "code": "DE",
        "population": 83000000
    }
    courty.add_country(new_country)
    
    # Update it
    result = courty.update_country("DE", {"population": 83200000})
    assert result == True
    
    # Verify update
    germany = courty.get_country_by_code("DE")
    assert germany['population'] == 83200000
    
    # Test invalid code
    invalid = courty.update_country("XX", {"population": 100})
    assert invalid == False
    
    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)
    
    print("✓ test_update_country passed")


def run_all_tests():
    """运行所有测试 / Run all tests"""
    print("开始测试... / Starting tests...\n")
    
    tests = [
        test_initialization,
        test_get_all_countries,
        test_get_country_by_code,
        test_get_country_by_name,
        test_search_countries,
        test_add_country,
        test_update_country
    ]
    
    failed = 0
    for test in tests:
        try:
            test()
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
    
    print(f"\n测试完成 / Tests completed")
    print(f"通过: {len(tests) - failed}/{len(tests)}")
    print(f"失败: {failed}/{len(tests)}")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
