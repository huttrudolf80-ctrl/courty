#!/usr/bin/env python3
"""
交互式示例 / Interactive Example
演示如何使用Courty API / Demonstrates how to use the Courty API
"""

from courty import CountryData


def demo():
    """演示API使用 / Demonstrate API usage"""
    print("=" * 60)
    print("Courty - 国家信息查询工具演示")
    print("Courty - Country Information Query Tool Demo")
    print("=" * 60)
    
    # 初始化 / Initialize
    print("\n1. 初始化数据管理器 / Initialize data manager")
    courty = CountryData()
    print("   CountryData() 已创建 / created")
    
    # 获取所有国家 / Get all countries
    print("\n2. 获取所有国家 / Get all countries")
    countries = courty.get_all_countries()
    print(f"   共有 {len(countries)} 个国家 / Total {len(countries)} countries:")
    for c in countries:
        print(f"   - {c['name']} ({c['name_en']})")
    
    # 按代码查询 / Query by code
    print("\n3. 按代码查询国家 / Query country by code")
    code = "CN"
    country = courty.get_country_by_code(code)
    if country:
        print(f"   代码 {code} 查询结果 / Query result for code {code}:")
        print(f"   名称 / Name: {country['name']} ({country['name_en']})")
        print(f"   首都 / Capital: {country['capital']} ({country['capital_en']})")
        print(f"   人口 / Population: {country['population']:,}")
        print(f"   面积 / Area: {country['area_km2']:,} km²")
    
    # 按名称查询（中文）/ Query by name (Chinese)
    print("\n4. 按中文名称查询 / Query by Chinese name")
    name = "日本"
    country = courty.get_country_by_name(name)
    if country:
        print(f"   '{name}' 的信息 / Information for '{name}':")
        print(f"   代码 / Code: {country['code']}")
        print(f"   首都 / Capital: {country['capital']}")
    
    # 按名称查询（英文）/ Query by name (English)
    print("\n5. 按英文名称查询 / Query by English name")
    name = "United Kingdom"
    country = courty.get_country_by_name(name)
    if country:
        print(f"   '{name}' 的信息 / Information for '{name}':")
        print(f"   中文名 / Chinese name: {country['name']}")
        print(f"   代码 / Code: {country['code']}")
    
    # 搜索特定大洲 / Search by continent
    print("\n6. 搜索亚洲国家 / Search Asian countries")
    asian_countries = courty.search_countries(continent="亚洲")
    print(f"   找到 {len(asian_countries)} 个亚洲国家 / Found {len(asian_countries)} Asian countries:")
    for c in asian_countries:
        print(f"   - {c['name']} ({c['name_en']})")
    
    # 搜索欧洲国家 / Search European countries
    print("\n7. 搜索欧洲国家 / Search European countries")
    european_countries = courty.search_countries(continent_en="Europe")
    print(f"   找到 {len(european_countries)} 个欧洲国家 / Found {len(european_countries)} European countries:")
    for c in european_countries:
        print(f"   - {c['name']} ({c['name_en']})")
    
    print("\n" + "=" * 60)
    print("演示完成！/ Demo completed!")
    print("提示 / Tip: 运行 'python3 courty.py' 查看更多示例")
    print("Tip: Run 'python3 courty.py' to see more examples")
    print("=" * 60)


if __name__ == "__main__":
    demo()
