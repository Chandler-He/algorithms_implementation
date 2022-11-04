print("Welcome!!!")
print("The test cases are imported to the program!")
print("*"*50)
while True:
    def print_subsets (head, list, count):
        # head means the prefix of the list;
        # count means how many sets elements you want;
        list = filter(list)  
        #call back filter func; 
        if count == 0:
            #judge if your desire sets value is zero, then return none;
            print(head)
            return 0
        for i in range(len(list)):
            # for loop for traverse all the values in the list;
            print_subsets("%s%s"%(head,list[i]), list[i+1:], count - 1)
            # output logic, with prefix of the list and current list location, then list append, and count reverse.
    def filter(list):
        str_f = ''
        # def a empty string
        for i in list:
            if i.isdigit() == True:
                # judge if is number, then only take digits, abondon commas;
                str_f += i
        return str_f
    
    print_subsets ("", input("Please input the data: "), 4)
    print("*"*50)
    
    
