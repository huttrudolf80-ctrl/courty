# Courty - 国家信息查询工具

一个简单易用的国家信息管理工具，方便Copilot传递和获取国家数据。

A simple and easy-to-use country information management tool that makes it convenient for Copilot to pass and retrieve country data.

## 功能特性 / Features

- 📊 **丰富的国家数据** - 包含国家名称（中英文）、代码、首都、人口、面积等信息
- 🔍 **灵活查询** - 支持通过国家代码、名称、大洲等多种方式查询
- ✏️ **数据管理** - 支持添加、更新国家信息
- 🌐 **双语支持** - 完整的中英文双语支持
- 🚀 **易于集成** - 简单的Python API，易于扩展为REST API

## 快速开始 / Quick Start

### 基本使用 / Basic Usage

```python
from courty import CountryData

# 创建数据管理器 / Create data manager
courty = CountryData()

# 获取所有国家 / Get all countries
countries = courty.get_all_countries()

# 通过代码查询 / Query by code
china = courty.get_country_by_code("CN")
print(china['name'])  # 输出: 中国

# 通过名称查询 / Query by name
us = courty.get_country_by_name("United States")
print(us['capital_en'])  # 输出: Washington D.C.

# 搜索亚洲国家 / Search Asian countries
asian = courty.search_countries(continent="亚洲")
```

### 运行示例 / Run Example

```bash
python3 courty.py
```

## 数据结构 / Data Structure

国家数据存储在 `countries.json` 文件中，每个国家包含：

Country data is stored in `countries.json`, each country includes:

- `id` - 唯一标识符 / Unique identifier
- `name` - 中文名称 / Chinese name
- `name_en` - 英文名称 / English name
- `code` - ISO国家代码 / ISO country code
- `capital` - 首都中文名 / Capital Chinese name
- `capital_en` - 首都英文名 / Capital English name
- `population` - 人口 / Population
- `area_km2` - 面积(平方公里) / Area in km²
- `continent` - 大洲中文名 / Continent Chinese name
- `continent_en` - 大洲英文名 / Continent English name

## API 文档 / API Documentation

查看 [API_EXAMPLES.md](API_EXAMPLES.md) 了解更多使用示例，包括：

See [API_EXAMPLES.md](API_EXAMPLES.md) for more usage examples, including:

- Python API详细用法 / Detailed Python API usage
- REST API示例 / REST API examples
- 数据格式说明 / Data format specification

## 主要方法 / Main Methods

- `get_all_countries()` - 获取所有国家 / Get all countries
- `get_country_by_code(code)` - 通过代码查询 / Query by code
- `get_country_by_name(name)` - 通过名称查询 / Query by name
- `add_country(data)` - 添加国家 / Add country
- `update_country(code, updates)` - 更新国家 / Update country
- `search_countries(**filters)` - 搜索国家 / Search countries

## 许可 / License

MIT
