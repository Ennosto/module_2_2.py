first = int(input('Первое число: '))
second = int(input('Второе число: '))
third = int(input('Третье число: '))
if first == second and second == third and third == first:
    print('3')
elif first == second and second == third and third == first:
    print('0')
elif first == second or second == third or third == first:
    print('2')
#Вроде так, но можно сжульничать и убрав нестрогие условия:
#if first == second and second == third and third == first:
    #print('3')
#elif first != second and second != third and third != first:
    #print('0')
#else:
    #print('2')
# Мягкие параметры, наверное лучше ставить в конце конструкта.
#Либо же оставить мягкие, но вторым и else применить для тех случаев,
# когда все три числа не равны.
# Также можно убрать один or, оставив под ДЗ, чтобы выполнялось равенство 1 и 3.
# И так же последним условием.

#Интересно, что в лекции о not ничего нет, а в дз есть. Погуглил, побаловался.
#У меня всегда ощущение, что можно сделать компактнее. 