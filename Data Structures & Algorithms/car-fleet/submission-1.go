import "slices"

func carFleet(target int, position []int, speed []int) int {
	// sort the car fleet by the position, keeping speed intact as well
	type car struct{
		position  int
		speed  int
	}
	cars := []car{}
	st := []float32{}
	var timetaken func(car) float32
	timetaken = func(c car) float32{
		fpos := float32(c.position)
		fsp := float32(c.speed)
		return (float32(target)-fpos)/fsp
	}
	for ind, _ := range speed{
		temp := car{
			position: position[ind],
			speed: speed[ind],
		}
		cars = append(cars, temp)
	}
	slices.SortFunc(cars, func(a,b car) int{
		return b.position - a.position
	})

	fmt.Println(cars)
	for _, val := range cars{
		fmt.Println("bfore",st)
		if len(st) == 0{
			st = append(st, timetaken(val))
			fmt.Println("after",st)
			continue
		}

		if timetaken(val) > st[len(st)-1]{
			// if time taken is greater, this would become a new fleet
			st = append(st, timetaken(val))
		}
		fmt.Println("after",st)
	}
	return len(st)
}
