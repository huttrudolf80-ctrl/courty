#!/usr/bin/env python3
"""
Courty - 国家信息查询工具
Country Information Query Tool

方便Copilot传递和获取国家数据
Makes it easy for Copilot to pass and retrieve country data
"""

import json
import os
from typing import List, Dict, Optional


class CountryData:
    """国家数据管理类 / Country Data Manager"""
    
    def __init__(self, data_file: str = "countries.json"):
        """
        初始化国家数据管理器
        Initialize country data manager
        
        Args:
            data_file: JSON数据文件路径 / Path to JSON data file
        """
        self.data_file = data_file
        self.countries = []
        self.load_data()
    
    def load_data(self) -> None:
        """
        从JSON文件加载国家数据
        Load country data from JSON file
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.countries = data.get('countries', [])
        else:
            self.countries = []
    
    def save_data(self) -> None:
        """
        保存国家数据到JSON文件
        Save country data to JSON file
        """
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump({'countries': self.countries}, f, ensure_ascii=False, indent=2)
    
    def get_all_countries(self) -> List[Dict]:
        """
        获取所有国家信息
        Get all country information
        
        Returns:
            所有国家的列表 / List of all countries
        """
        return self.countries
    
    def get_country_by_code(self, code: str) -> Optional[Dict]:
        """
        通过国家代码查询国家信息
        Query country information by country code
        
        Args:
            code: 国家代码（如 CN, US, JP）/ Country code (e.g., CN, US, JP)
        
        Returns:
            国家信息字典或None / Country information dict or None
        """
        for country in self.countries:
            if country.get('code', '').upper() == code.upper():
                return country
        return None
    
    def get_country_by_name(self, name: str) -> Optional[Dict]:
        """
        通过国家名称查询国家信息（支持中英文）
        Query country information by name (supports Chinese and English)
        
        Args:
            name: 国家名称 / Country name
        
        Returns:
            国家信息字典或None / Country information dict or None
        """
        for country in self.countries:
            if country.get('name') == name or country.get('name_en') == name:
                return country
        return None
    
    def add_country(self, country_data: Dict) -> bool:
        """
        添加新的国家信息
        Add new country information
        
        Args:
            country_data: 国家信息字典 / Country information dict
        
        Returns:
            是否添加成功 / Whether addition was successful
        """
        # 检查必需字段 / Check required fields
        required_fields = ['name', 'name_en', 'code']
        if not all(field in country_data for field in required_fields):
            return False
        
        # 检查是否已存在 / Check if already exists
        if self.get_country_by_code(country_data['code']):
            return False
        
        # 设置ID / Set ID
        if 'id' not in country_data:
            max_id = max([c.get('id', 0) for c in self.countries], default=0)
            country_data['id'] = max_id + 1
        
        self.countries.append(country_data)
        self.save_data()
        return True
    
    def update_country(self, code: str, updates: Dict) -> bool:
        """
        更新国家信息
        Update country information
        
        Args:
            code: 国家代码 / Country code
            updates: 要更新的字段 / Fields to update
        
        Returns:
            是否更新成功 / Whether update was successful
        """
        for i, country in enumerate(self.countries):
            if country.get('code', '').upper() == code.upper():
                self.countries[i].update(updates)
                self.save_data()
                return True
        return False
    
    def search_countries(self, **filters) -> List[Dict]:
        """
        根据条件搜索国家
        Search countries by criteria
        
        Args:
            **filters: 搜索条件（如 continent="亚洲"）/ Search criteria
        
        Returns:
            符合条件的国家列表 / List of matching countries
        """
        results = []
        for country in self.countries:
            match = True
            for key, value in filters.items():
                if country.get(key) != value:
                    match = False
                    break
            if match:
                results.append(country)
        return results


def main():
    """示例用法 / Example usage"""
    # 创建国家数据管理器 / Create country data manager
    courty = CountryData()
    
    print("=== 所有国家 / All Countries ===")
    for country in courty.get_all_countries():
        print(f"{country['name']} ({country['name_en']}) - {country['code']}")
    
    print("\n=== 查询中国信息 / Query China Info ===")
    china = courty.get_country_by_code("CN")
    if china:
        print(json.dumps(china, ensure_ascii=False, indent=2))
    
    print("\n=== 搜索亚洲国家 / Search Asian Countries ===")
    asian_countries = courty.search_countries(continent="亚洲")
    for country in asian_countries:
        print(f"{country['name']} ({country['name_en']})")


if __name__ == "__main__":
    main()
