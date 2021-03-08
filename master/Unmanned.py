def Unmanned(L, N, track):
   result = 0
   current_location = 0
   dict = {0:'range', 1:'red_light', 2:'green_light'}
   point_dict = 0
   current_point = 1
   traffic_light_time = 0
   red_time = -1
   green_time = -1

   for list in track:
       for element in list:
           if point_dict == 0:
               result += element - current_location #ride to next traffic light
               current_location = element
               traffic_light_time = result
               point_dict = 1
           elif point_dict == 1: #red
               red_time = element
               point_dict = 2
           else: #green
               green_time = element
               point_dict = 0

           if red_time != -1 and green_time != -1:
               time_to_green = result
               green_counter = green_time
               while True:
                   if time_to_green == 0:
                       break
                   time_to_green -= red_time
                   green_counter = green_time
                   if time_to_green <= 0:
                       break
                   else:
                       while green_counter != 0:
                           time_to_green -= 1
                           green_counter -= 1
                           if time_to_green == 0:
                               break
               result -= time_to_green
               red_time = -1
               green_time = -1

   result += L - current_location

   return result