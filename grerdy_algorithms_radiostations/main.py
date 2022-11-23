#create set "states_needed"

states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

#create the dictionary "stations" wich keys are names of radio station

stations={
    "kone": {"id", "nv", "ut"},
    "ktwo": {"wa", "id", "mt"},
    "kthree": {"or", "nv", "ca"},
    "kfour": {"nv", "ut"},
    "kfive": {"ca", "az"}
}

final_stations = set()
while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        # Создаем переменную "covered", которая хранит множество штатов,
        # которые еще не покрыты и которые могут быть покрыты текущей радиостанцией "station".
        # Мы находимо это множество путем пересечения следующих множеств:
        # 1. "states_needed" - множество еще не покрытых штатов.
        # 2. "states_for_station" - множество штатов, которые может покрыть текущяя радиостанция "station".
        # ----------
        # Create the variable "covered" that stores a set of states
        # that are not yet covered and can be covered by the current radio station "station".
        # We find this set by intersecting the following sets:
        # 1. "states_needed" - the set of the states that are not yet covered.
        # 2. "states_for_station" - the set of the states that can be covered by the current radio station "station".
        covered = states_needed & states_for_station
        # Если множество "covered" больше, чем множество "states_covered", то
        # ----------
        # If the set "covered" is greater than the set "states_covered", then
        if len(covered) > len(states_covered):
            # текущая радиостанция "station" становится новой лучшей радиостанцией "best_station",
            # ----------
            # the current radio station "station" becomes the new best radio station "best_station",
            best_station = station
            # а также мы обновляем множество "states_covered".
            # ----------
            # and also we update the set "states_covered".
            states_covered = covered
        # После работы каждого цикла for мы уменьшаем перечень штатов, которые необходимо покрыть,
        # вычитая список штатов, которые покрываются текущей лучшей радиостанцией "best_station".
        # Мы это делаем путем вычитания из множества "states_needed" множества "states_covered".
        # ----------
        # After each cycle of the for loop, we reduce the list of the states to be covered
        # by subtracting the list of the states that are covered by the current best radio station "best_station".
        # We do this by subtracting the set "states_covered" from the set "states_needed".
    states_needed -= states_covered
    # А также после работы каждого цикла for мы добавляем текущуюю лучшую радиостанцию "best_station"
    # в итоговый набор радиостанций "final_stations".
    # Для добавления нового элемента в множества мы используем метод "add".
    # ----------
    # And also after each cycle of the for loop, we add the current best radio station "best_station"
    # to the final set of radio stations "final_stations".
    final_stations.add(best_station)

# Выводим на экран итоговый набор радиостанций для покрытия штатов "final_stations".
# Функция "print()" выводит некую указанную информацию на экран или на какое-либо другое устройство вывода.
# ----------
# Display the final set of the radio stations to cover the states "final_stations".
# The function "print()" prints the specified message to the screen, or other standard output device.
print(final_stations)





