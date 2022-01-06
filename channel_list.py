channel_list=[] ## Start with an empty list

channelNumber = int(input())     # Get the first input, channel number

while channelNumber != 0:           # While the channelNumber 0
    channelNumber -= 1                  # count down
    channel_data = input().split(';')     # get channel data
    channel_list.append(channel_data)         # Add it to a list
    
## We now have a array of all channels (which are themselves, lists)

## Now we need the last two inputs, premium_value and not_premium
premium_content_price=float(input())
regular_content_price=float(input())

# first write bonus
print("-----")
print("BÔNUS")
print("-----")
for channel in channel_list:
    channel_name=channel[0]
    subscribers=int(channel[1])
    payment=float(channel[2])
    is_premium=channel[3]

    if(is_premium == "não"):
        bonus = (subscribers // 1000) * regular_content_price
    else:
        bonus = (subscribers // 1000) * premium_content_price

    total = (payment+bonus)
    total_as_currency = "R$ {:.2f}".format(total)
    
    print('{}: {}'.format(channel_name,total_as_currency)) ## Show the chanel & total
