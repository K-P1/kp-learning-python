from faker import Faker

fake = Faker("ar_SA")

print(fake.name())
print(fake.email())
print(fake.first_name())
print(fake.last_name())
print(fake.phone_number())
print(fake.address())
print(fake.text())

print(fake.name_male())
print(fake.name_female())
print(fake.job())
print(fake.word())
print(fake.words(7))
print(fake.currency())
print(fake.currency_name())
print(fake.currency_code())


