type Item struct{
	value string
	time int
}
type TimeMap struct {
	m map[string][]Item
}

func Constructor() TimeMap {
	m := make(map[string][]Item)
	t := TimeMap{
		m: m,
	}
	return t
}

func (this *TimeMap) Set(key string, value string, timestamp int) {
	t := Item{
		value: value,
		time: timestamp,
	}
	
	// initalize if nil
	if this.m[key] == nil{
		this.m[key] = []Item{}
	}

	this.m[key] = append(this.m[key],t)
	fmt.Println(this.m)
}

func (this *TimeMap) Get(key string, timestamp int) string {
	list, ok := this.m[key]
	if !ok{
		return "" // does not exist
	}
	
	probableAns := ""
	left := 0
	right := len(list) - 1

	for left <= right{
		mid := (left+right)/2
		cur := list[mid]
		fmt.Println(list, left, right, cur, timestamp)

		if cur.time == timestamp{
			return cur.value
		}else if cur.time > timestamp{
			right = mid - 1
		}else{
			probableAns = cur.value
			left = mid + 1
		}
	}
	fmt.Println(probableAns)
	
	return probableAns


}
