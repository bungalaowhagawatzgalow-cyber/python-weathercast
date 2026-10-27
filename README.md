# Python Weathercast

A Python weather application that retrieves current weather conditions for cities around the world using Open-Meteo.

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Status](https://img.shields.io/badge/Status-In_Development-orange?style=flat)
![Requests](https://img.shields.io/badge/Library-Requests-2E6F9E?style=flat)
![Geopy](https://img.shields.io/badge/Library-Geopy-4B8BBE?style=flat)
![Weather API](https://img.shields.io/badge/Weather_API-Open--Meteo-00A98F?style=flat)
![Geocoding](https://img.shields.io/badge/Geocoding-Nominatim-blue?style=flat)

## Features

- Search for weather by city and country
- Choose Celsius, Fahrenheit, or Kelvin
- View current temperature
- Check relative humidity and wind speed
- View precipitation and cloud cover
- Display local time and timezone information

## Built With

- **Python 3.14** — Main programming language
- **Requests** — HTTP requests to the weather API
- **Geopy** — Geocoding city names into coordinates
- **Open-Meteo API** — Weather data provider
- **Nominatim** — Location search

## Installation

### Clone the repository

```bash
git clone https://github.com/bungalaowhagawatzgalow-cyber/python-weathercast.git
cd python-weathercast
```

### Install dependencies

```bash
pip install requests geopy
```

### Run the application

```bash
python weatherapp.py
```

If needed, use `python3` instead of `python`.

## Usage

1. Start the application.
2. Choose your preferred temperature unit.
3. Enter a city and country.
4. View the current weather information.

## Data Sources

- [Open-Meteo](https://open-meteo.com/) — Weather data
- [Nominatim](https://nominatim.org/) — Geocoding and location lookup

## Future Improvements

- [x] Search weather by city and country
- [x] Choose Celsius, Fahrenheit, or Kelvin
- [x] Display current temperature
- [x] Show humidity and wind speed
- [x] Allow multiple searches in one session
- [ ] Add a graphical user interface
- [ ] Display multi-day forecasts
- [ ] Improve error handling

## License

This project is licensed under the [MIT License](LICENSE).

---

*Built as part of my python learning journey*
