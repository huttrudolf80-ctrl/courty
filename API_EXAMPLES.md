# API 使用示例 / API Usage Examples

## Python API 使用 / Python API Usage

```python
from courty import CountryData

# 创建数据管理器 / Create data manager
courty = CountryData()

# 获取所有国家 / Get all countries
all_countries = courty.get_all_countries()

# 通过代码查询 / Query by code
china = courty.get_country_by_code("CN")
print(china)

# 通过名称查询 / Query by name
japan = courty.get_country_by_name("日本")
print(japan)

# 搜索特定大洲的国家 / Search countries by continent
asian_countries = courty.search_countries(continent="亚洲")

# 添加新国家 / Add new country
new_country = {
    "name": "德国",
    "name_en": "Germany",
    "code": "DE",
    "capital": "柏林",
    "capital_en": "Berlin",
    "population": 83149300,
    "area_km2": 357022,
    "continent": "欧洲",
    "continent_en": "Europe"
}
courty.add_country(new_country)

# 更新国家信息 / Update country information
courty.update_country("DE", {"population": 83200000})
```

## 命令行使用 / Command Line Usage

```bash
# 运行示例 / Run example
python3 courty.py

# 在Python REPL中使用 / Use in Python REPL
python3 -i courty.py
>>> courty = CountryData()
>>> courty.get_country_by_code("US")
```

## REST API 示例 / REST API Example

使用Flask创建简单的REST API / Create simple REST API with Flask:

```python
from flask import Flask, jsonify, request
from courty import CountryData

app = Flask(__name__)
courty = CountryData()

@app.route('/api/countries', methods=['GET'])
def get_countries():
    """获取所有国家 / Get all countries"""
    return jsonify(courty.get_all_countries())

@app.route('/api/countries/<code>', methods=['GET'])
def get_country(code):
    """获取指定国家 / Get specific country"""
    country = courty.get_country_by_code(code)
    if country:
        return jsonify(country)
    return jsonify({"error": "Country not found"}), 404

@app.route('/api/countries', methods=['POST'])
def add_country():
    """添加国家 / Add country"""
    data = request.json
    if courty.add_country(data):
        return jsonify({"success": True}), 201
    return jsonify({"error": "Failed to add country"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

启动服务 / Start service:
```bash
pip install flask
python3 api_example.py
```

访问API / Access API:
```bash
# 获取所有国家 / Get all countries
curl http://localhost:5000/api/countries

# 获取指定国家 / Get specific country
curl http://localhost:5000/api/countries/CN

# 添加国家 / Add country
curl -X POST http://localhost:5000/api/countries \
  -H "Content-Type: application/json" \
  -d '{"name":"德国","name_en":"Germany","code":"DE",...}'
```

## 数据格式 / Data Format

每个国家包含以下字段 / Each country contains the following fields:

```json
{
  "id": 1,
  "name": "中国",              // 中文名称 / Chinese name
  "name_en": "China",          // 英文名称 / English name
  "code": "CN",                // ISO国家代码 / ISO country code
  "capital": "北京",           // 首都中文名 / Capital Chinese name
  "capital_en": "Beijing",     // 首都英文名 / Capital English name
  "population": 1411778724,    // 人口 / Population
  "area_km2": 9596961,         // 面积(平方公里) / Area in km²
  "continent": "亚洲",         // 大洲中文名 / Continent Chinese name
  "continent_en": "Asia"       // 大洲英文名 / Continent English name
}
```
