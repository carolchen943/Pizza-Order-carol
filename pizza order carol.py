from tkinter import *
 
from tkinter.scrolledtext import *
import tkinter.messagebox #Messagebox

class Main:
    def __init__(self, parent):
        
        self.WIDTH = 1000
        self.HEIGHT = 700
        self.num_cols = 3
        self.num_rows = 2
        global images
        global gou_images
        self.totalprice = 0
        images = []
        gou_images = []
        self.ReNum = [0,0,0,0,0,0] #create list of the number shown in the number counter, with the initial numbers 0.
        self.GouNum = [0,0,0,0,0,0] #create list of the number shown in the number counter, with the initial numbers 0.
        self.pizzanum = []
        root.geometry('{}x{}'.format(self.WIDTH,self.HEIGHT))
        self.total = 0
        # the users cannot change the size of the window
        root.resizable(0, 0)
        
        self.regular_name = [
            'Margherita', 'Kiwi', 'Garlic', 'Cheese', 'Hawaiian', 'Mediterranean (vegan)'
        ]
        self.regular_img = [
            'img/Margherita.gif', 'img/Kiwi.gif', 'img/Garlic.gif', 'img/Cheese.gif',
            'img/Hawaiian.gif', 'img/Mediterranean (vegan).gif'
        ]
        self.regular_content = [
            'Fresh tomato, mozzarella, fresh basil, parmesan', 'Bacon, egg, mozzarella',
            'Mozzarella, garlic', 'Mozzarella, oregano',
            'Ham, pineapple, mozzarella', 'Lebanese herbs, olive oil, fresh tomatoes, olives, onion'
        ]
        self.gourmet_name = [
            'Meat', 'Chicken Cranberry', 'Satay Chicken', 'Big BBQ Bacon', 'Veggie', 'Meatlovers'
        ]
        self.gourmet_img = [
            'img/Meat.gif', 'img/Chicken Cranberry.gif', 'img/Satay Chicken.gif', 'img/Big BBQ Bacon.gif',
            'img/Veggie.gif', 'img/Meatlovers.gif'
        ]
        self.gourmet_content = [
            'Bacon, pancetta, ham, onion, pepperoni, mozzarella', 'Smoked chicken, cranberry, camembert mozzarella',
            'Smoked chic, onions, capsicum, pine nuts, satay sauce, mozzarella Chilli flakes and dried basil',
            'Smoky Bacon served on our classic marinara tomato sauce, heaped with mozzarella, topped off with a sweet and tangy BBQ drizzle', 
            'sweet red onion, mushroom, red capsicum & melting mozzarella with drizzles of our tangy roast capsicum drizzle, finished with a dash of oregano',
            'Spicy pepperoni, Italian sausage, succulent ham, seasoned ground beef and crispy bacon all piled onto classic marinara sauce and finished with cheesy mozzarella and a drizzle of BBQ'
        ]

       

        # create a canva
        self.f = Frame(parent, relief=FLAT, bd=-2, bg='linen')
        self.f.place(x=0, y=80, width=self.WIDTH, height=self.HEIGHT-80)

        self.canvas = Canvas(self.f, bd=-2)
        self.frame = Frame(self.canvas, bd=-2, bg='white', width=self.WIDTH, height=self.HEIGHT-80)
        
        self.myscrollbar = Scrollbar(
            self.f, 
            orient=VERTICAL, 
            command=self.canvas.yview
        )  # SCROLL BAR   ####
        self.canvas.configure(yscrollcommand=self.myscrollbar.set)
        self.myscrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.pack(side=LEFT)
        self.canvas.create_window((0, 0), window=self.frame)
        self.frame.bind("<Configure>", self.myfunction)

        #create top menu frame
        self.frame1 = Frame(parent, bg="linen", padx=30)
        self.frame1.grid(row = 0, columnspan = 7)
        #welcome label
        welcome_label = Label(self.frame1, text = "Welcome to Heavenly Pizza!", bg = "linen", font=("Conmic Sans MS","20","bold"), fg = "red")
        welcome_label.grid(row=0, column=0, sticky = W, padx = 5, pady = 10)
        #logout button
##        logout_btn = Button(self.frame1, text = "Log out", bg = "linen", font=("Conmic Sans MS","20","bold"), fg = "red")
##        logout_btn.grid(row=0, column=1, sticky = W, padx = 12, pady = 15)
        #regular pizza menu button
        regular_btn = Button(self.frame1, text = "Regular pizzas ", bg = "linen", font=("Conmic Sans MS","20","bold"), fg = "coral", command = self.regular)
        regular_btn.grid(row=0, column=2, sticky = W, padx = 15, pady = 10)
        #gourmet pizza menu button
        gourmet_btn = Button(self.frame1, text = "Gourmet pizzas", bg = "linen", font=("Conmic Sans MS","20","bold"), fg = "coral", command = self.gourmet)
        gourmet_btn.grid(row=0, column=3, sticky = W, padx = 12, pady = 10)
        #check out button
        checkout_btn = Button(self.frame1, text = "Checkout", bg = "linen", font=("Conmic Sans MS","20","bold"), fg = "red", command = self.checkout)
        checkout_btn.grid(row=0, column=4, sticky = W, padx = 15, pady = 10)
        #cart button
##        cart_btn = Button(self.frame1, text = "CART", bg = "linen", font=("Conmic Sans MS","20","bold"), fg = "red")
##        cart_btn.grid(row=0, column=5, sticky = W, padx = 12, pady = 15)
        #total button
        self.total_label = Label(self.frame1, text = "Total = $ 0", bg = "linen", font=("Conmic Sans MS","20","bold"), fg = "red")
        self.total_label.grid(row=0, column=5, sticky = W, padx = 15, pady = 10)

       
        #######################################################
        
        self.regular_frame = Frame(self.frame, bg="linen", width = self.WIDTH, height = self.HEIGHT)
        self.gourmet_frame = Frame(self.frame, bg="linen", width = self.WIDTH, height = self.HEIGHT)
        self.deliverycheckout_frame = Frame(self.frame, bg="linen", width = self.WIDTH, height = self.HEIGHT)
        self.checkout_frame = Frame(self.frame, bg="linen", width = self.WIDTH, height = self.HEIGHT)
        self.pickupcheckout_frame = Frame(self.frame, bg="linen", width = self.WIDTH, height = self.HEIGHT)

        self.readfile_frame = Frame(self.frame, bg="linen", width = self.WIDTH, height = self.HEIGHT)

        
        #default get in the regular page first 
        self.regular()

    # def myfunction(self):
    #     self.canvas.configure(scrol)


   
        

    def myfunction(self, event):
        self.canvas.configure(
            scrollregion=self.canvas.bbox("all"), width=self.WIDTH-20, height=self.HEIGHT-60
        )



    def regular(self):
        self.readfile_frame.grid_forget()
        
        self.gourmet_frame.grid_forget()
        self.deliverycheckout_frame.grid_forget()
        # self.canvas.create_window((0, 30),  window=self.regular_frame)    
        self.regular_frame.grid(row = 1, columnspan = 4) 
        self.pickupcheckout_frame.grid_forget()
        self.checkout_frame.grid_forget()
        #product frame
        self.re_product_frame = []
        for i in range(len(self.regular_name)):
            self.re_product_frame.append(Frame(self.regular_frame, bg="linen", width = self.WIDTH, height = 60))
        frame_count = 0
        for c in range(self.num_cols):
            for r in range(self.num_rows):
                if frame_count < len(self.regular_name):
                    self.re_product_frame[frame_count].grid(row = r, column = c)
                    frame_count += 1
        #names and images of each regular pizza
        self.re_name_label = []
        self.re_img_label = []
        self.re_content_label = []
        self.re_price_label = []
        self.re_reduce_num_btn = []
        self.re_num_label = []
        self.re_add_num_btn = []
        self.re_add_cart_btn = []
        i = 0
        
        # images = []
        for r in self.regular_img:
            images.append(PhotoImage(file = r))
        # print(images)
        for i in range(len(self.regular_name)):
            #print(i, len(self.product_frame), regular_name,images[i])
            self.re_name_label.append(Label(self.re_product_frame[i], text = self.regular_name[i], font=("Conmic Sans MS","20","bold"), fg = "dimgray", bg="linen"))
            self.re_name_label[i].grid(row = 0, column = 0, sticky = N+W+S+E, pady = 5)

            self.re_img_label.append(Label(self.re_product_frame[i], image=images[i]))
            self.re_img_label[i].grid(row = 1, column = 0)
            
            self.re_content_label.append(Label(self.re_product_frame[i], text = self.regular_content[i], bg="linen"))
            self.re_content_label[i].grid(row = 2, column = 0, sticky = N+W+S+E, pady = 3)

            self.re_price_label.append(Label(self.re_product_frame[i], text = "$10", font=("Conmic Sans MS","16","bold"), fg = "red", bg="linen"))
            self.re_price_label[i].grid(row = 3, column = 0, sticky = W, padx = 50)

            self.re_reduce_num_btn.append(Button(self.re_product_frame[i], text = "-", command =lambda x=i: self.re_ReduceNumber(x)))
            self.re_reduce_num_btn[i].grid(row = 3, column = 0, sticky = E, pady = 15, padx = 80)

            self.re_num_label.append(Label(self.re_product_frame[i], text = self.ReNum[i]))
            self.re_num_label[i].grid(row = 3, column = 0, sticky = E, pady = 15, padx = 50)
            
            self.re_add_num_btn.append(Button(self.re_product_frame[i], text = "+", command =lambda x=i: self.re_AddNumber(x)))
            self.re_add_num_btn[i].grid(row = 3, column = 0, sticky = E, pady = 15, padx = 20)
            
##            self.re_add_cart_btn.append(Button(self.re_product_frame[i], text = "ADD TO CART", fg = "red"))
##            self.re_add_cart_btn[i].grid(row = 4, column = 0, sticky = N+W+S+E, pady = 1)
   
        # self.frame2.grid(row = 1, columnspan = 4)
        # self.frame2.grid_propagate(0)
#create gourment pizza product frames
        gou_num_cols = 3
        gou_num_rows = 6
        self.gou_product_img_frame = []
        self.gou_product_text_frame = []
        self.gou_name_label = []
        self.gou_img_label = []
        self.gou_price_label = []
        self.gou_content_label = []
        self.gou_reduce_num_btn = []
        self.gou_num_label = []
        self.gou_add_num_btn = []
        self.gou_add_cart_btn = []
#########gourment part###########
        
    def gourmet(self):
        self.readfile_frame.grid_forget()

        self.checkout_frame.grid_forget()
        #create gourment frame
        self.regular_frame.grid_forget()
        self.deliverycheckout_frame.grid_forget()
        self.pickupcheckout_frame.grid_forget()
        ##self.gourment_frame.grid(row = 0, columnspan = 3)        
        # self.canvas.create_window((0, 30), window=self.gourment_frame)
        self.gourmet_frame.grid(row = 1, columnspan = 3)
        # self.regular_frame.grid_propagate(0)
        gou_num_cols = 3
        gou_num_rows = 6
        
        i = 0
        #create gourment pizza images list
        # gou_images = []
        for r in self.gourmet_img:
            gou_images.append(PhotoImage(file = r))
        #divide the whole big gourment frame into 6*3 small product frames, with the arrangment of the first column is used to display images,
        #the second is used to display labels(names, contents) and add-to-cart button, the third column is totally empty.
        #I'm planning to define the width and height of the first and the second column.
        frame_count = 0
        for c in range(gou_num_cols):
            if c == 0:
                for r in range(gou_num_rows):
                    self.gou_product_img_frame.append(Frame(self.gourmet_frame, bg="linen", width = 300, height = 200))
                    self.gou_product_img_frame[r].grid(row = r, column = c)
                    self.gou_product_img_frame[r].grid_propagate(0) 
            
                # if frame_count < (len(gourment_name))*3: #loop 6*3 times, since there are 6*3 grids in total
            # if c == 0: #At first column, I'm planning to add images, with width and height setted. 
            elif c == 1:
                for r in range(gou_num_rows):
                    self.gou_product_text_frame.append(Frame(self.gourmet_frame, bg="linen", width = 441, height = 200))
                    self.gou_product_text_frame[r].grid(row = r, column = c)
                    self.gou_product_text_frame[r].grid_propagate(0)
                
            # elif c == 1: #At second column, I'm planning to add labels&button(name,content, add-to-cart button), with width and height setted.
            #     self.gou_product_frame.append(Frame(self.gourment_frame, bg="linen", width = 100, height = 50))
            #     self.gou_product_frame[frame_count].grid(row = r, column = c)
            #     self.gou_product_frame[frame_count].grid_propagate(0)
                
            # else:  #refers to the third column, which have nothing in them, so no width and height needed.
            #     self.gou_product_frame.append(Frame(self.gourment_frame, bg="linen"))
            #     self.gou_product_frame[frame_count].grid(row = r, column = c)
                                           
            frame_count += 1

        #the names,images, add-to-cart buttons of each gourment pizza in each gourment product frame
        for i in range(len(self.gourmet_name)):
            #print(i, len(self.product_frame), regular_name,images[i])
            
            self.gou_img_label.append(Label(self.gou_product_img_frame[i], image=gou_images[i], padx = 50, bg="linen"))
            self.gou_img_label[i].grid(row = 0, column = 0)

            self.gou_name_label.append(Label(self.gou_product_text_frame[i], text = self.gourmet_name[i], font=("Conmic Sans MS","20","bold"), fg = "dimgray", bg="linen"))
            self.gou_name_label[i].grid(row = 0, column = 1, sticky = W, pady = 0, padx = 25)
            
            self.gou_content_label.append(Label(self.gou_product_text_frame[i], text = self.gourmet_content[i], wraplength = 400, justify = 'left', bg="linen"))
            self.gou_content_label[i].grid(row = 1, column = 1, sticky = N+S+E+W, pady = 0, padx = 25)

            self.gou_price_label.append(Label(self.gou_product_text_frame[i], text = "$17", font=("Conmic Sans MS","20","bold"), fg = "red", bg="linen"))
            self.gou_price_label[i].grid(row = 2, column = 1, sticky = W, pady = 15, padx = 40)

            self.gou_reduce_num_btn.append(Button(self.gou_product_text_frame[i], text = "-", command =lambda x=i: self.gou_ReduceNumber(x)))
            self.gou_reduce_num_btn[i].grid(row = 2, column = 1, sticky = E, pady = 40, padx = 100)

            self.gou_num_label.append(Label(self.gou_product_text_frame[i], text = self.GouNum[i]))
            self.gou_num_label[i].grid(row = 2, column = 1, sticky = E, pady = 40, padx = 68)
            
            self.gou_add_num_btn.append(Button(self.gou_product_text_frame[i], text = "+", command =lambda x=i: self.gou_AddNumber(x)))
            self.gou_add_num_btn[i].grid(row = 2, column = 1, sticky = E, pady = 40, padx = 40)   
            
##            self.gou_add_cart_btn.append(Button(self.gou_product_text_frame[i], text = "ADD TO CART", fg = "red"))
##            self.gou_add_cart_btn[i].grid(row = 3, column = 1, sticky = S, pady =0, padx = 0)
            # i += 1


################################
    #self.totalprice = 0 
    def re_AddNumber(self,x):         
        re_index = self.re_add_num_btn.index(self.re_add_num_btn[x]) #find the index of the current button that user clicked in the cutton list
        self.ReNum[re_index] += 1 #Once click one of the buttons at a time, it will add one number
        #total number in the ReNum list
        re_total = 0 
        for item in self.ReNum:
            re_total += item
        #total number in the GouNum list
        gou_total = 0
        for item in self.GouNum:
            gou_total += item
        #total number that the user already ordered
        self.total = re_total + gou_total

        if self.total >5: #set maximum number that each user can order for each pizza
            self.ReNum[re_index] = self.ReNum[re_index]-(self.total-5)#let the current number counter stop on the current number (as it cannot be more than 5 pizzas)
            
            self.re_num_label[re_index].configure(text = self.ReNum[re_index])
            self.totalprice += 0
            if self.total == 6:
                get_help=Help()#connect to the Help class
                get_help.help_text.configure(text="Sorry, you cannot order more than 5 pizzas in total!")
        elif self.ReNum[re_index] >= 0:
            
            self.re_num_label[re_index].configure(text = self.ReNum[re_index])
            self.totalprice += 10
            self.total_label.configure(text = "Total = $"+str(self.totalprice))
        
            
        print(self.total, ":", self.regular_name[x])
        #self.total_label.configure(text = "Total = $"+(str(self.ReNum[re_index])*10))

    def re_ReduceNumber(self,x):        
        re_index = self.re_reduce_num_btn.index(self.re_reduce_num_btn[x])
        self.ReNum[re_index] -= 1
        if self.ReNum[re_index] >= 0 and self.ReNum[re_index] <=5:
            
            self.re_num_label[x].configure(text = self.ReNum[re_index])                 
            self.totalprice -= 10
            self.total_label.configure(text = "Total = $"+str(self.totalprice))
            self.total -= 1
        elif self.ReNum[re_index] < 0:
            self.ReNum[re_index] = 0
            
            self.re_num_label[re_index].configure(text = self.ReNum[re_index])        


################################       
    def gou_AddNumber(self,x):                     
        gou_index = self.gou_add_num_btn.index(self.gou_add_num_btn[x]) #find the index of the current button that user clicked in the cutton list
        self.GouNum[gou_index] += 1 #Once click one of the buttons at a time, it will add one number
        #total number in the ReNum list
        re_total = 0 
        for item in self.ReNum:
            re_total += item
        #total number in the GouNum list
        gou_total = 0
        for item in self.GouNum:
            gou_total += item
        #total number that the user already ordered
        self.total = re_total + gou_total

        if self.total >5: #set maximum number that each user can order for each pizza
            self.GouNum[gou_index] = self.GouNum[gou_index]-(self.total-5)#let the current number counter stop on the current number (as it cannot be more than 5 pizzas)
            
            self.gou_num_label[gou_index].configure(text = self.GouNum[gou_index])
            
            get_help=Help()#connect to the Help class
            get_help.help_text.configure(text="Sorry, you cannot order more than 5 pizzas in total!")


        elif self.GouNum[gou_index] >= 0:
                 
            self.gou_num_label[gou_index].configure(text = self.GouNum[gou_index])
            self.totalprice += 17
            self.total_label.configure(text = "Total = $"+str(self.totalprice))
        
        print(self.total, ":", self.gourmet_name[x])
        
        
    def gou_ReduceNumber(self,x):
        try:
            gou_index = self.gou_reduce_num_btn.index(self.gou_reduce_num_btn[x])
            self.GouNum[gou_index] -= 1
            if self.GouNum[gou_index] >= 0 and self.GouNum[gou_index] <=5:            
                self.gou_num_label[x].configure(text = self.GouNum[gou_index])                 
                self.totalprice -= 17
                self.total_label.configure(text = "Total = $"+str(self.totalprice))
                self.total -= 1
            elif self.GouNum[gou_index] < 0:
                self.GouNum[gou_index] = 0            
                self.gou_num_label[gou_index].configure(text = self.GouNum[gou_index])
        except Exception as e:
            print(e)
            return False
        finally:
            return True

########### No Exception Process###########################
##        gou_index = self.gou_reduce_num_btn.index(self.gou_reduce_num_btn[x])
##        self.GouNum[gou_index] -= 1
##        if self.GouNum[gou_index] >= 0 and self.GouNum[gou_index] <=5:            
##            self.gou_num_label[x].configure(text = self.GouNum[gou_index])                 
##            self.totalprice -= 17
##            self.total_label.configure(text = "Total = $"+str(self.totalprice))
##        elif self.GouNum[gou_index] < 0:
##            self.GouNum[gou_index] = 0            
##            self.gou_num_label[gou_index].configure(text = self.GouNum[gou_index])

            

    def checkout(self):

        if self.total == 0:
            tkinter.messagebox.showwarning('Warning','You have not order anything!')
        else:
            self.readfile_frame.grid_forget() 

            self.regular_frame.grid_forget()
            self.gourmet_frame.grid_forget()
            self.deliverycheckout_frame.grid_forget()
            self.pickupcheckout_frame.grid_forget()
            self.checkout_frame.grid(row = 1, columnspan = 3)
            Label(self.checkout_frame, text = "TO START YOUR ORDER, SELECT AN ORDER TYPE BELOW:" , font=("Conmic Sans MS","25","bold"), bg = 'linen',
                   ).grid(row=1,columnspan=2, sticky = EW,padx=0,pady=30)
            Button(self.checkout_frame, text = "PICK UP" , font=("Conmic Sans MS","25","bold"), bg = 'linen',
                   width = 15, height = 15, command = self.pickupcheckout).grid(row=2,column=0, sticky = W,padx=50,pady=20)
            Button(self.checkout_frame, text = "DELIVERY" , font=("Conmic Sans MS","25","bold"), bg = 'linen',
                   width = 15, height = 15, command = self.deliverycheckout).grid(row=2,column=1, sticky = W,padx=50,pady=20)

        

    def deliverycheckout(self):
        self.readfile_frame.grid_forget()

        self.regular_frame.grid_forget()
        self.gourmet_frame.grid_forget()
        self.checkout_frame.grid_forget()
        self.pickupcheckout_frame.grid_forget()
        self.deliverycheckout_frame.grid(row = 1, columnspan = 3)
        Label(self.deliverycheckout_frame, text='Name:', font=("Conmic Sans MS","15","bold"), bg = 'linen').grid(row=1,column=0, sticky = E,padx=1,pady=10)
        self.v1 = StringVar()
        e1 = Entry(self.deliverycheckout_frame,textvariable=self.v1,width=80)
        e1.grid(row=1,column=1,padx=1,pady=10)         

        Label(self.deliverycheckout_frame, text='Address:', font=("Conmic Sans MS","15","bold"), bg = 'linen').grid(row=2,column=0, sticky = E,padx=1,pady=10)
        self.v2 = StringVar()
        e2 = Entry(self.deliverycheckout_frame,textvariable=self.v2,width=80)
        e2.grid(row=2,column=1,padx=1,pady=10)          

        Label(self.deliverycheckout_frame, text='Telephone:', font=("Conmic Sans MS","15","bold"), bg = 'linen').grid(row=3,column=0, sticky = E,padx=1,pady=10)
        self.v3 = StringVar()
        e3 = Entry(self.deliverycheckout_frame,textvariable=self.v3,width=80)
        e3.grid(row=3,column=1,padx=1,pady=10)    

        Label(self.deliverycheckout_frame, text='Email:', font=("Conmic Sans MS","15","bold"), bg = 'linen').grid(row=4,column=0, sticky = E,padx=1,pady=10)
        self.v4 = StringVar()
        e4 = Entry(self.deliverycheckout_frame,textvariable=self.v4,width=80)
        e4.grid(row=4,column=1,padx=1,pady=10)

        Label(self.deliverycheckout_frame, text='Your Order: ', font=("Conmic Sans MS","15","bold"), bg = 'linen').grid(row=5,column=0, sticky = NE,padx=1,pady=10)
        self.showorder = ScrolledText(self.deliverycheckout_frame, width=55, height=10, wrap='word')
        self.showorder.grid(row=5,column=1,padx=1,pady=10, columnspan=1, sticky = W)


        Label(self.deliverycheckout_frame, text='Order Type: ', font=("Conmic Sans MS","15","bold"), bg = 'linen').grid(row=8,column=0, sticky = E,padx=1,pady=10)

        Label(self.deliverycheckout_frame, text='Delivery  +  $10', font=("Conmic Sans MS","15","bold"), bg = 'linen').grid(row=8,column=1, sticky = W,padx=1,pady=10)
            
        Label(self.deliverycheckout_frame, text='Total Price:', font=("Conmic Sans MS","15","bold"), bg = 'linen').grid(row=11,column=0, sticky = E,padx=1,pady=10)
        Label(self.deliverycheckout_frame, text= ' $ '+str(self.totalprice + 10), font=("Conmic Sans MS","20","bold"), bg = 'linen').grid(row=12,column=1, sticky = W,padx=1,pady=10)

        Button(self.deliverycheckout_frame, text='Place Order', font=("Conmic Sans MS","20","bold"), fg = "red"
               , command = lambda x=self: deliveryPlaceOrder(x)).grid(row=13,column=1,padx=1,pady=10, sticky = E)
        Button(self.deliverycheckout_frame, text='Reselect An Order Type', font=("Conmic Sans MS","20","bold"), fg = "red", command = self.checkout).grid(row=13,column=1,padx=1,pady=10, sticky = W)
 

        self.pizzanum = []

        for i in range(6):           
            if self.ReNum[i] > 0:
                self.pizzanum.append(self.regular_name[i]+"       x"+str(self.ReNum[i]))
            if self.GouNum[i] > 0:
                self.pizzanum.append(self.gourmet_name[i]+"       x"+str(self.GouNum[i]))
        for i in self.pizzanum: 
            self.showorder.insert(END, '%s\n'%i)
            

    def pickupcheckout(self):
        self.readfile_frame.grid_forget()

        self.regular_frame.grid_forget()
        self.gourmet_frame.grid_forget()
        self.checkout_frame.grid_forget()
        self.pickupcheckout_frame.grid(row = 1, columnspan = 3)
        self.deliverycheckout_frame.grid_forget()
        Label(self.pickupcheckout_frame, text='Name:', font=("Conmic Sans MS","15","bold"), bg = 'linen').grid(row=1,column=0, sticky = E,padx=1,pady=10)
        self.v1 = StringVar()
        e1 = Entry(self.pickupcheckout_frame,textvariable=self.v1,width=80)
        e1.grid(row=1,column=1,padx=1,pady=10)         

##        Label(self.pickupcheckout_frame, text='Address:', font=("Conmic Sans MS","15","bold"), bg = 'linen').grid(row=2,column=0, sticky = E,padx=1,pady=10)
##        v2 = StringVar()
##        e2 = Entry(self.pickupcheckout_frame,textvariable=v2,width=80)
##        e2.grid(row=2,column=1,padx=1,pady=10)          

        Label(self.pickupcheckout_frame, text='Telephone:', font=("Conmic Sans MS","15","bold"), bg = 'linen').grid(row=3,column=0, sticky = E,padx=1,pady=10)
        self.v3 = StringVar()
        e3 = Entry(self.pickupcheckout_frame,textvariable=self.v3,width=80)
        e3.grid(row=3,column=1,padx=1,pady=10)

        Label(self.pickupcheckout_frame, text='Email:', font=("Conmic Sans MS","15","bold"), bg = 'linen').grid(row=4,column=0, sticky = E,padx=1,pady=10)
        self.v4 = StringVar()
        e4 = Entry(self.pickupcheckout_frame,textvariable=self.v4,width=80)
        e4.grid(row=4,column=1,padx=1,pady=10)

        Label(self.pickupcheckout_frame, text='Your Order: ', font=("Conmic Sans MS","15","bold"), bg = 'linen').grid(row=5,column=0, sticky = NE,padx=1,pady=10)
        self.showorder = ScrolledText(self.pickupcheckout_frame, width=55, height=10, wrap='word')
        self.showorder.grid(row=5,column=1,padx=1,pady=10, columnspan=1, sticky = W)


        Label(self.pickupcheckout_frame, text='Order Type: ', font=("Conmic Sans MS","15","bold"), bg = 'linen').grid(row=8,column=0, sticky = E,padx=1,pady=10)

        Label(self.pickupcheckout_frame, text='Pick Up', font=("Conmic Sans MS","15","bold"), bg = 'linen').grid(row=8,column=1, sticky = W,padx=1,pady=10)
            
        Label(self.pickupcheckout_frame, text='Total Price:', font=("Conmic Sans MS","15","bold"), bg = 'linen').grid(row=11,column=0, sticky = E,padx=1,pady=10)
        Label(self.pickupcheckout_frame, text= ' $ '+str(self.totalprice), font=("Conmic Sans MS","20","bold"), bg = 'linen').grid(row=12,column=1, sticky = W,padx=1,pady=10)

        Button(self.pickupcheckout_frame, text='Place Order', font=("Conmic Sans MS","20","bold"), fg = "red"
               , command = lambda x=self: pickupPlaceOrder(x)).grid(row=13,column=1,padx=1,pady=10, sticky = E)
        Button(self.pickupcheckout_frame, text='Reselect An Order Type', font=("Conmic Sans MS","20","bold"), fg = "red", command = self.checkout).grid(row=13,column=1,padx=1,pady=10, sticky = W)
        self.pizzanum = []

        for i in range(6):           
            if self.ReNum[i] > 0:
                self.pizzanum.append(self.regular_name[i]+"       x"+str(self.ReNum[i]))
            if self.GouNum[i] > 0:
                self.pizzanum.append(self.gourmet_name[i]+"       x"+str(self.GouNum[i]))
        for i in self.pizzanum: 
            self.showorder.insert(END, '%s\n'%i)        
        
        

#******************************************************
class deliveryPlaceOrder:
    def __init__(self, Main):
        background="linen"
        self.top = Toplevel()
        self.top.title('Check Out')
         
        Label(self.top, text='Name:').grid(row=1,column=0, sticky = E,padx=1,pady=1)
        L1 = Label(self.top,text=Main.v1.get())
        L1.grid(row=1,column=1,padx=1,pady=1, sticky = W)         
        ############check if name is empty #################
        if Main.v1.get()=='':
            print(Main.v1.get())
            tkinter.messagebox.showwarning('Warning','Please input your name!')
            self.close_deliverywindow()
            return
        ########################################################
        Label(self.top, text='Address:').grid(row=2,column=0, sticky = E,padx=1,pady=1)
        L2 = Label(self.top,text=Main.v2.get())
        L2.grid(row=2,column=1,padx=1,pady=1, sticky = W)          

        ############ check if Address is empty ##################
        if Main.v2.get()=='':
            print(Main.v2.get())
            tkinter.messagebox.showwarning('Warning','Please input Address!')
            self.close_deliverywindow()
            return
        ##################################################################


        Label(self.top, text='Telephone:').grid(row=3,column=0, sticky = E,padx=1,pady=1)
        L3 = Label(self.top,text=Main.v3.get())
        L3.grid(row=3,column=1,padx=1,pady=1, sticky = W)           

        ############ check if telephone number is valid ##################
        ############ Using try...except to capture exception #############
#        if type(Main.v3.get())!=float:
        if Main.v3.get()=='':
            tkinter.messagebox.showwarning('Warning','please input digit number telephone!')
            self.close_deliverywindow()            
            return                
        ##########set restriction of digital number of phone number#########
        elif len(Main.v3.get())!=7 and len(Main.v3.get())!=10:
            tkinter.messagebox.showwarning('Warning','please check if the phone number is wrong as normal phone number is either 10-digit or 7-digit!')
            self.close_deliverywindow()            
            return
        #################
        else:
            try:
                float(Main.v3.get())
            except Exception as e:
#                tkinter.messagebox.showwarning('Warning',str(e)+'please input digit number for telephone!')
                tkinter.messagebox.showwarning('Warning, telephone number error','Please input digit number for telephone!')
                self.close_deliverywindow()                
                return
        ##################################################################
        

        Label(self.top, text='Email:').grid(row=4,column=0, sticky = E,padx=1,pady=1)
        L4 = Label(self.top,text=Main.v4.get())
        L4.grid(row=4,column=1,padx=1,pady=1, sticky = W)
        ############check if email is empty #################
        if Main.v4.get()=='':
            print(Main.v4.get())
            tkinter.messagebox.showwarning('Warning','Please input your email!')
            self.close_deliverywindow()
            return
        ########################################################

        showorderlabel = []
        Label(self.top, text='Your Order: ').grid(row=5,column=0, sticky = E,padx=1,pady=1)
        for item in Main.pizzanum:         
            showorderlabel.append(Label(self.top, text=item))
        for i in range(len(Main.pizzanum)):
            showorderlabel[i].grid(row=5+i,column=1, sticky = W,padx=1,pady=1)


        Label(self.top, text='Order Type: ').grid(row=10,column=0, sticky = E,padx=1,pady=1)

        Label(self.top, text='Delivery + $10').grid(row=10,column=1, sticky = W,padx=1,pady=1)
            
        Label(self.top, text='Total Price:').grid(row=11,column=0, sticky = E,padx=1,pady=1)
        Label(self.top, text= ' $ '+str(Main.totalprice+10)).grid(row=12,column=1, sticky = W,padx=1,pady=1)

        Button(self.top, text='OK', command=self.close_deliverywindow).grid(row=13,column=1,padx=1,pady=20, sticky = W)

        ##########write order informaton to 'orderinfo.txt'##########
        f = open('orderinfo.txt', 'a') # append information    
        orderline=Main.v1.get()+","+Main.v2.get()+","+Main.v3.get()+","+Main.v4.get()+","+str(Main.pizzanum)+","+'Delivery fee $10'+","+"$"+str(Main.totalprice+10)+"\n"
        print(orderline)
        f.write(orderline)    
        f.close()
        #############################################################
        
        
    def close_deliverywindow(self):
        self.top.destroy()
        buttons.ReNum = [0,0,0,0,0,0]
        buttons.GouNum = [0,0,0,0,0,0]      
        
        buttons.totalprice=0        
       
        

#******************************************************
class pickupPlaceOrder:
    def __init__(self, Main):
        background="linen"
        self.top = Toplevel()
        self.top.title('Check Out')
         
        Label(self.top, text='Name:').grid(row=1,column=0, sticky = E,padx=1,pady=1)
        L1 = Label(self.top,text=Main.v1.get())
        L1.grid(row=1,column=1,padx=1,pady=1, sticky = W)         
        ############check if name is empty #################
        if Main.v1.get()=='':
            print(Main.v1.get())
            tkinter.messagebox.showwarning('Warning','Please input your name!')
            self.close_pickupwindow()
            return
        ########################################################
##        Label(self.top, text='Address:').grid(row=2,column=0, sticky = E,padx=1,pady=1)
##        L2 = Label(self.top,text=Main.v2.get())
##        L2.grid(row=2,column=1,padx=1,pady=1, sticky = W)          

        Label(self.top, text='Telephone:').grid(row=3,column=0, sticky = E,padx=1,pady=1)
        L3 = Label(self.top,text=Main.v3.get())
        L3.grid(row=3,column=1,padx=1,pady=1, sticky = W)

        ############ Check if telephone number is valid ##################
        ############ Using try...except to capture exception #############
        if Main.v3.get()=='':
            tkinter.messagebox.showwarning('Warning','please input digit number telephone!')
            self.close_pickupwindow()            
            return                
        ##########set restriction of digital number of phone number#########
        elif len(Main.v3.get())!=7 and len(Main.v3.get())!=10:
            tkinter.messagebox.showwarning('Warning','please check if the phone number is wrong as normal phone number is either 10-digit or 7-digit!')
            self.close_pickupwindow()            
            return
        #################
        else:
            try:
                float(Main.v3.get())
            except Exception as e:
#                tkinter.messagebox.showwarning('Warning',str(e)+'please input digit number for telephone!')
                tkinter.messagebox.showwarning('Warning, telephone number error','Please input digit number for telephone!')
                self.close_pickupwindow()                
                return

##        try:
##            float(Main.v3.get())
##        except Exception as e:
###            tkinter.messagebox.showwarning('Warning, telephone number error',str(e)+'please input digit number for telephone!')
##            tkinter.messagebox.showwarning('Warning, telephone number error','please input digit number for telephone!')
##            self.close_pickupwindow()
##            return
        ##################################################################

        
        Label(self.top, text='Email:').grid(row=4,column=0, sticky = E,padx=1,pady=1)
        L4 = Label(self.top,text=Main.v4.get())
        L4.grid(row=4,column=1,padx=1,pady=1, sticky = W)
        showorderlabel = []
        ############check if email is empty #################
        if Main.v4.get()=='':
            print(Main.v4.get())
            tkinter.messagebox.showwarning('Warning','Please input your email!')
            self.close_pickupwindow()
            return
        ###########################################################
        Label(self.top, text='Your Order: ').grid(row=5,column=0, sticky = E,padx=1,pady=1)
        for item in Main.pizzanum:         
            showorderlabel.append(Label(self.top, text=item))
        for i in range(len(Main.pizzanum)):
            showorderlabel[i].grid(row=5+i,column=1, sticky = W,padx=1,pady=1)


        Label(self.top, text='Order Type: ').grid(row=10,column=0, sticky = E,padx=1,pady=1)

        Label(self.top, text='Pick Up').grid(row=10,column=1, sticky = W,padx=1,pady=1)
            
        Label(self.top, text='Total Price:').grid(row=11,column=0, sticky = E,padx=1,pady=1)
        Label(self.top, text= ' $ '+str(Main.totalprice)).grid(row=12,column=1, sticky = W,padx=1,pady=1)

        Button(self.top, text='OK', command=self.close_pickupwindow).grid(row=13,column=1,padx=1,pady=20, sticky = W)

        
        
        
    def close_pickupwindow(self):        
        self.top.destroy()
        buttons.ReNum = [0,0,0,0,0,0]
        buttons.GouNum = [0,0,0,0,0,0]      
                
        buttons.totalprice=0       

        
        
#******************************************
class Help:
    def __init__(self):
        background="white"
        self.help_box=Toplevel()
        self.help_frame=Frame(self.help_box, width=300,height=200, bg=background)
        self.help_frame.grid()
        heading = Label(self.help_frame, text="Notice", font="arial 10 bold", bg=background)
        heading.grid(column=0, row=0)
        self.help_text = Label(self.help_frame, text=" ", justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(column=0, row=1)
        dismiss_btn = Button(self.help_frame, text="ok", width=10, bg="blue",
                             font="arial 10 bold", command=self.close_help)
        dismiss_btn.grid(row=2, pady=10)
        
    def close_help(self):
        self.help_box.destroy() 
      

#main
if __name__ == '__main__':
    root = Tk()
    buttons = Main(root)
    root.title ("Heavenly Pizza GUI Ordering System")
    
    root.mainloop()
