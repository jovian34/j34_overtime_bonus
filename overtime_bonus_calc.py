import collections

base_rate = 11.1
base_rate = base_rate * 1.1

WeekTiers = collections.namedtuple('WeekTiers',
                                   'tier1, tier2, tier3')

week_1 = WeekTiers(tier1=75, tier2=150, tier3=200)
week_2 = WeekTiers(tier1=125, tier2=200, tier3=250)
week_3 = WeekTiers(tier1=175, tier2=250, tier3=300)
week_4 = WeekTiers(tier1=225, tier2=300, tier3=350)

weeks = { 1: week_1,
          2: week_2,
          3: week_3,
          4: week_4}

day_map = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
           4: 'Thursday', 5: 'Friday', 6: 'Saturday'}


def enter_weeks_on_bonus():
    weeks_on_bonus = input('How many prior weeks in a row on bonus? ')
    weeks_on_bonus = int(weeks_on_bonus) + 1
    if weeks_on_bonus > 4:
        weeks_on_bonus = 4
    return weeks_on_bonus


def enter_hours_worked():
    hours_worked_per_day = []
    for i in range(7):
        hours = float(input(f'How many hours did you work on {day_map[i]}? '))
        hours_worked_per_day.append(hours)
    return hours_worked_per_day


def calculate_pay_per_day(base_rate, hours_worked):

    sunday_rate = 2.5 * base_rate
    sunday_pay = float(hours_worked[0]) * sunday_rate
    print(f'On Sunday you earned ${sunday_rate:4.2f} per hour for a total of ${sunday_pay:6.2f}')
    total_pay = sunday_pay
    total_hours = float(hours_worked[0])

    ot_hours = hours_worked[0]

    for i in range(1, 7):
        if hours_worked[i] == 0:
            pass
        else:
            week_ot = total_hours + float(hours_worked[i]) - 40 - ot_hours
            day_ot = float(hours_worked[i]) - 10
            if week_ot > 0 and day_ot < week_ot:
                day_ot = week_ot
            if day_ot < 0:
                day_ot = 0
            day_ot = float(day_ot)
            reg_hours = float(hours_worked[i]) - day_ot
            if reg_hours < 0:
                reg_hours = 0
            reg_pay = reg_hours * base_rate
            print(f'On {day_map[i]} you worked {reg_hours} regular hours for ${reg_pay:6.2f}')
            total_pay += reg_pay
            if day_ot > 0:
                ot_pay = day_ot * base_rate * 1.5
                print(f'On {day_map[i]} you worked {day_ot} overtime hours for ${ot_pay:6.2f}')
                total_pay += ot_pay
                ot_hours += day_ot
            total_hours += reg_hours + day_ot

    return total_pay, total_hours


def calc_bonus(total_hours, bonus_week, adjust):
    total_hours += adjust
    if total_hours >= 55:
        bonus = weeks[bonus_week].tier3
    elif total_hours >= 50:
        bonus = weeks[bonus_week].tier2
    elif total_hours >= 45:
        bonus = weeks[bonus_week].tier1
    else:
        bonus = 0
    return float(bonus)


def enter_adjustment():
    return int(input('Enter week adjustment: '))


def main():
    bonus_week = enter_weeks_on_bonus()
    adjust = enter_adjustment()
    hours_worked = enter_hours_worked()
    total_pay, total_hours = calculate_pay_per_day(base_rate, hours_worked)
    print(f'You earned ${total_pay:6.2f} before bonus.')
    bonus = calc_bonus(total_hours, bonus_week, adjust)
    print(f"You earned a bonus of ${bonus:6.2f}.")
    total_pay += bonus
    final_rate = total_pay / total_hours
    print(f'Your average rate of pay for this week was ${final_rate:4.2f} per hour.')
    print(f'You worked {total_hours:4.2f} hours and earned ${total_pay:6.2f} for the week.')


if __name__ == '__main__':
    main()