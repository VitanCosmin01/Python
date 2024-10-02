# pip install countryinfo
from countryinfo import CountryInfo

country = CountryInfo(input("enter country name: "))

print("Country name: ", country.name().capitalize())
print("Country capital: ", country.capital())
print("Country population: ", country.population())
print("Country currencies: ", country.currencies())
print("Country area: ", country.area())
print("Country languages: ", country.languages())
print("Country timezones: ", country.timezones())
print("Country region: ", country.region())
print("Country subregion: ", country.subregion())
print("Country borders: ", country.borders())
