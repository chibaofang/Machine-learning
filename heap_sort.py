def adjust_heap(lists, i, size):
  l_child = 2 * i + 1
  r_child = 2 * i + 2
  max = i
  if i < size/2:
    if l_child < size and lists[l_child] > lists[max]:
      max = l_child
    if r_child < size and lists[r_child] > lists[max]:
      max = r_child
    if max != i:
      lists[max], lists[i] = lists[i], lists[max]
      adjust_heap(lists, max, size)

def build_heap(lists, size):
  for i in range(0, (size/2))[::-1]:
    ajust_heap(lists, i, size)

def heap_sort(lists):
  size = len(lists)
  build_heap(lists, size)
  for i in range(0, size)[::-1]:
    lists[0], lists[i] = lists[i], lists[0]
    ajust_heap(lists, 0, i)

  
