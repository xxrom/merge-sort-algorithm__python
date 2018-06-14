# сортировка слиянием
# O(N * logN) всегда и стабильно
# метод стабильный, не in-State(нужно дополнительно N памяти)
# По сути разбиваем пополам массив, пока он не будет единичный и
# потом начинаем объединять кусочки постепенно, сравнивая их
# каждый раз просто идем с начала подмассива и выбираем MIN из них

def mergeSort(array):
  if len(array) > 1:
    print('len = %s ' % len(array))

    middle = len(array) // 2
    leftArray = mergeSort(array[0: middle])
    rightArray = mergeSort(array[middle: len(array)])

    print('left array', leftArray)
    print('right array', rightArray)

    # сортируем array, учитывая leftArray и rightArray
    mergeArray(array, leftArray, rightArray)

  return array

# объединяем два массива в один с помощью сравнения посимвольного
def mergeArray(array, leftArray, rightArray):
  leftIndex = 0
  rightIndex = 0
  arrayIndex = 0

  while leftIndex < len(leftArray) and rightIndex < len(rightArray):
    if leftArray[leftIndex] <= rightArray[rightIndex]:
      print('l %s ' % leftArray[leftIndex])
      array[arrayIndex] = leftArray[leftIndex]
      leftIndex += 1

    else:
      print('l %s ' % rightArray[rightIndex])
      array[arrayIndex] = rightArray[rightIndex]
      rightIndex += 1

    arrayIndex += 1

  # если остались не добавленные элементы в левом массиве
  if leftIndex < len(leftArray):
    # add left Items
    for i in range(leftIndex, len(leftArray)):
      array[arrayIndex] = leftArray[i]
      arrayIndex += 1
  else:
    # add right Items
    for i in range(rightIndex, len(rightArray)):
      array[arrayIndex] = rightArray[i]
      arrayIndex += 1

# test
if __name__ == '__main__':
  unsortedArray = [0, -3, 3, 100, 32, 200, -324, 324, 33, -1]
  print(mergeSort(unsortedArray))

