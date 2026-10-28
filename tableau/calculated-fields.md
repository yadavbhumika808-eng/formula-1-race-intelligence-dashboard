# Tableau Calculated Fields (validate field names first)

## Win Flag
```tableau
IF [finish_position] = 1 THEN 1 ELSE 0 END
```

## Podium Flag
```tableau
IF [finish_position] <= 3 THEN 1 ELSE 0 END
```

## Positions Gained
```tableau
[grid_position] - [finish_position]
```

## DNF Flag
```tableau
IF [dnf] = 1 THEN 1 ELSE 0 END
```

## Average Lap Time (seconds)
Use `AVG([lap_time_s])` from `lap_intelligence`.

## Pole-to-Win indicator
At race-driver grain, compare `qualifying_position = 1` with `finish_position = 1`. Match by `race_id` and driver.
