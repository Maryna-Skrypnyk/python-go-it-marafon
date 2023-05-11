
DAYS_OF_WEEK = ["понеділок", "вівторок", "середа", "четвер", "п'ятниця"]
WEEKEND = ["субота", "неділя"]


print()
day_of_week = input("Введіть день тижня: ").lower()

if day_of_week in DAYS_OF_WEEK:
    print()
    print("Сьогодні на роботу")
elif day_of_week in WEEKEND:
    print()
    print("Сьогодні вихідний")
else:
    print()
    print("Такого дня не існує")
    


