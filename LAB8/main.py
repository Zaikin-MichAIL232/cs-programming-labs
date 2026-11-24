def is_valid_command(command):
    return command in ("0", "1", "2", "exit")


def can_burn(power, fuel):
    return fuel >= power


def simulate_step(height, speed, fuel, power, gravity, thrust_step):
    new_fuel = fuel - power

    new_speed = speed + gravity - thrust_step * power
    if new_speed < 0:
        new_speed = 0

    new_height = height - new_speed
    if new_height < 0:
        new_height = 0

    return new_height, new_speed, new_fuel


def get_status(height, speed, safe_limit=2):
    if height > 0:
        return "В полете"
    elif height == 0:
        if speed <= safe_limit:
            return "Посадка успешна"
        else:
            return "Авария"


def format_state(height, speed, fuel):
    return f"Высота: {height} | Скорость: {speed} | Топливо: {fuel}"


def main():
    height = 30
    speed = 2
    fuel = 12
    gravity = 3
    thrust_step = 2
    safe_limit = 2
    print(format_state(height, speed, fuel))

    while True:
        command = input()

        if not is_valid_command(command):
            print("Ошибка команды")
            continue

        if command == "exit":
            print("Полет прерван")
            break

        power = int(command)

        if not can_burn(power, fuel):
            print("Недостаточно топлива")
            continue

        # Выполнение шага
        height, speed, fuel = simulate_step(height, speed, fuel, power, gravity, thrust_step)


        print(format_state(height, speed, fuel))


        status = get_status(height, speed, safe_limit)
        if status != "В полете":
            print(status)
            break


if __name__ == "__main__":
    main()