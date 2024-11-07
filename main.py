# числовые:
# int
number_1 = 12 

# float
number_2 = 15.5     

print(
    number_1,
    number_2,
)


#строки

string_1 = 'hello'
string_2 = "hello"
string_3 = "hello \\ \"world\" \\ "
string_4 = "\n"


print(
    string_1,
    string_4,
    string_2,
    string_4,
    string_3,
    )


string_5 = string_1.title()
string_6 = "string string STRING string string".title()

string_7 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius iaculis pulvinar. Sed in consequat leo, at sollicitudin lacus. Aenean non diam nec nulla lacinia fermentum eu non nisi. Curabitur nec libero imperdiet massa luctus luctus. Suspendisse pellentesque lacus sem, eu molestie ante scelerisque vel. Suspendisse sagittis efficitur orci, at rhoncus turpis elementum non. Sed interdum faucibus enim, vel aliquam nulla tempus eget. Fusce suscipit, ligula ac consequat volutpat, justo risus malesuada magna, at fringilla magna urna sed leo. Praesent sed auctor libero. Nam luctus vitae diam in consectetur. In vestibulum interdum nibh vitae efficitur. Aenean faucibus, velit sed venenatis ultricies, justo leo molestie urna, nec sollicitudin velit magna a arcu. Phasellus vestibulum vehicula justo, at vehicula felis congue quis. Aenean sodales pellentesque ipsum, vel vehicula lorem eleifend a. Proin eu quam vestibulum, tristique nunc nec, facilisis purus. Fusce vitae lorem quis tortor dapibus sodales."
string_8 = "Maecenas posuere dui id nulla mattis euismod. Quisque laoreet a nisl quis imperdiet. Duis sollicitudin ipsum in dictum convallis. Sed id elementum felis, vitae cursus mauris. Donec vitae blandit est. Cras vitae sagittis lorem. Pellentesque in ipsum fringilla, tristique mauris in, porttitor leo. Praesent sollicitudin nibh eros, vitae ornare sem faucibus ut. Suspendisse viverra felis a eros consectetur fringilla. Nullam efficitur ante eget auctor posuere. Sed purus enim, mattis in bibendum non, varius eu velit. Mauris commodo purus quis vulputate volutpat. Sed ullamcorper justo felis, aliquet iaculis massa gravida vitae. Fusce mollis massa quis metus accumsan, et iaculis est maximus."
string_9 = string_7 + string_8.upper()
string_10 = f'{string_1}, asdas, asd, {string_6}'

print(
    string_5,
    string_4,
    string_6,
    string_4,
    string_6.lower(),
    string_4,
    string_6.upper(),

    )

print(
    string_9,
    string_4,
    string_10,
    )


