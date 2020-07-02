from tkinter import *
#from PIL import ImageTk, Image 
class Main:
    def __init__(self, parent):
        
        self.WIDTH = 1000
        self.HEIGHT = 800
        self.num_cols = 3
        self.num_rows = 2
        global images
        global gou_images

        images = []
        gou_images = []

        root.geometry('{}x{}'.format(self.WIDTH,self.HEIGHT))
        # forbid user to resize the GUI window
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
        self.gourment_name = [
            'Meat', 'Chicken Cranberry', 'Satay Chicken', 'Big BBQ Bacon', 'Veggie', 'Meatlovers'
        ]
        self.gourment_img = [
            'img/Margherita.gif', 'img/Kiwi.gif', 'img/Garlic.gif', 'img/Cheese.gif',
            'img/Hawaiian.gif', 'img/Mediterranean (vegan).gif'
        ]
        self.gourment_content = [
            'Bacon, pancetta, ham, onion, pepperoni, mozzarella', 'Smoked chicken, cranberry, camembert mozzarella',
            'Smoked chic, onions, capsicum, pine nuts, satay sauce, mozzarella Chilli flakes and dried basil',
            'Smoky Bacon served on our classic marinara tomato sauce, heaped with mozzarella, topped off with a sweet and tangy BBQ drizzle', 
            'sweet red onion, mushroom, red capsicum & melting mozzarella with drizzles of our tangy roast capsicum drizzle, finished with a dash of oregano',
            'Spicy pepperoni, Italian sausage, succulent ham, seasoned ground beef and crispy bacon all piled onto classic marinara sauce and finished with cheesy mozzarella and a drizzle of BBQ'
        ]

       

        #create canvas
        self.f = Frame(parent, relief=FLAT, bd=-2)
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

        #top menu frame
        self.frame1 = Frame(parent, bg="linen", padx=30)
        self.frame1.grid(row = 0, columnspan = 7)
        #welcome label
        welcome_label = Label(self.frame1, text = "Welcome, ", bg = "linen", font=("Conmic Sans MS","20","bold"), fg = "red")
        welcome_label.grid(row=0, column=0, sticky = W, padx = 5, pady = 15)
        #logout button
        logout_btn = Button(self.frame1, text = "Log out", bg = "linen", font=("Conmic Sans MS","20","bold"), fg = "red")
        logout_btn.grid(row=0, column=1, sticky = W, padx = 12, pady = 15)
        #regular pizza menu button
        regular_btn = Button(self.frame1, text = "Regular pizzas ", bg = "linen", font=("Conmic Sans MS","20","bold"), fg = "red", command = self.regular)
        regular_btn.grid(row=0, column=2, sticky = W, padx = 12, pady = 15)
        #gourmet pizza menu button
        gourmet_btn = Button(self.frame1, text = "Gourmet pizzas", bg = "linen", font=("Conmic Sans MS","20","bold"), fg = "red", command = self.gourment)
        gourmet_btn.grid(row=0, column=3, sticky = W, padx = 12, pady = 15)
        #check out button
        checkout_btn = Button(self.frame1, text = "Checkout", bg = "linen", font=("Conmic Sans MS","20","bold"), fg = "red")
        checkout_btn.grid(row=0, column=4, sticky = W, padx = 12, pady = 15)
        #cart button
        cart_btn = Button(self.frame1, text = "CART", bg = "linen", font=("Conmic Sans MS","20","bold"), fg = "red")
        cart_btn.grid(row=0, column=5, sticky = W, padx = 12, pady = 15)
        #total button
        total_label = Label(self.frame1, text = "Total = ", bg = "linen", font=("Conmic Sans MS","20","bold"), fg = "red")
        total_label.grid(row=0, column=6, sticky = W, padx = 12, pady = 15)
        
        self.regular_frame = Frame(self.frame, bg="linen", width = self.WIDTH, height = self.HEIGHT)
        self.gourment_frame = Frame(self.frame, bg="linen", width = self.WIDTH, height = self.HEIGHT)

        #default get into regular page first
        self.regular()

    # def myfunction(self):
    #     self.canvas.configure(scrol)

    def myfunction(self, event):
        self.canvas.configure(
            scrollregion=self.canvas.bbox("all"), width=self.WIDTH-20, height=self.HEIGHT-60
        )



    def regular(self):
        self.gourment_frame.grid_forget()

        # self.canvas.create_window((0, 30),  window=self.regular_frame)    
        self.regular_frame.grid(row = 1, columnspan = 4) 
        
        #每个商品的小frame
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
            self.re_name_label.append(Label(self.re_product_frame[i], text = self.regular_name[i], font=("Conmic Sans MS","20","bold"), fg = "grey"))
            self.re_name_label[i].grid(row = 0, column = 0, sticky = N+W+S+E, pady = 5)

            self.re_img_label.append(Label(self.re_product_frame[i], image=images[i]))
            self.re_img_label[i].grid(row = 1, column = 0)
            
            self.re_content_label.append(Label(self.re_product_frame[i], text = self.regular_content[i]))
            self.re_content_label[i].grid(row = 2, column = 0, sticky = N+W+S+E, pady = 3)

            self.re_price_label.append(Label(self.re_product_frame[i], text = "$10", font=("Conmic Sans MS","16","bold"), fg = "red"))
            self.re_price_label[i].grid(row = 3, column = 0, sticky = W, padx = 50)

            self.re_reduce_num_btn.append(Button(self.re_product_frame[i], text = "-"))
            self.re_reduce_num_btn[i].grid(row = 3, column = 0, sticky = E, pady = 0, padx = 80)

            self.re_num_label.append(Label(self.re_product_frame[i], text = "0"))
            self.re_num_label[i].grid(row = 3, column = 0, sticky = E, pady = 0, padx = 50)
            
            self.re_add_num_btn.append(Button(self.re_product_frame[i], text = "+"))
            self.re_add_num_btn[i].grid(row = 3, column = 0, sticky = E, pady = 0, padx = 20)
            
            self.re_add_cart_btn.append(Button(self.re_product_frame[i], text = "ADD TO CART", fg = "red"))
            self.re_add_cart_btn[i].grid(row = 4, column = 0, sticky = N+W+S+E, pady = 1)
   
        # self.frame2.grid(row = 1, columnspan = 4)
        # self.frame2.grid_propagate(0)

    def gourment(self):
        #########gourment part###########
        #create gourment frame
        self.regular_frame.grid_forget()
        ##self.gourment_frame.grid(row = 0, columnspan = 3)        
        # self.canvas.create_window((0, 30), window=self.gourment_frame)
        self.gourment_frame.grid(row = 1, columnspan = 3)
        # self.regular_frame.grid_propagate(0)
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
        i = 0
        #create gourment pizza images list
        # gou_images = []
        for r in self.gourment_img:
            gou_images.append(PhotoImage(file = r))
        #divide the whole big gourment frame into 6*3 small product frames, with the arrangment of the first column is used to display images,
        #the second is used to display labels(names, contents) and add-to-cart button, the third column is totally empty.
        #I'm planning to define the width and height of the first and the second column.
        frame_count = 0
        for c in range(gou_num_cols):
            if c == 0:
                for r in range(gou_num_rows):
                    self.gou_product_img_frame.append(Frame(self.gourment_frame, bg="linen", width = 300, height = 200))
                    self.gou_product_img_frame[r].grid(row = r, column = c)
                    self.gou_product_img_frame[r].grid_propagate(0) 
            
                # if frame_count < (len(gourment_name))*3: #loop 6*3 times, since there are 6*3 grids in total
            # if c == 0: #At first column, I'm planning to add images, with width and height setted. 
            elif c == 1:
                for r in range(gou_num_rows):
                    self.gou_product_text_frame.append(Frame(self.gourment_frame, bg="linen", width = 441, height = 200))
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
        for i in range(len(self.gourment_name)):
            #print(i, len(self.product_frame), regular_name,images[i])
            
            self.gou_img_label.append(Label(self.gou_product_img_frame[i], image=gou_images[i], padx = 50))
            self.gou_img_label[i].grid(row = 0, column = 0)

            self.gou_name_label.append(Label(self.gou_product_text_frame[i], text = self.gourment_name[i], font=("Conmic Sans MS","20","bold"), fg = "grey"))
            self.gou_name_label[i].grid(row = 0, column = 1, sticky = W, pady = 0, padx = 25)
            
            self.gou_content_label.append(Label(self.gou_product_text_frame[i], text = self.gourment_content[i], wraplength = 400, justify = 'left'))
            self.gou_content_label[i].grid(row = 1, column = 1, sticky = N+S+E+W, pady = 0, padx = 25)

            self.gou_price_label.append(Label(self.gou_product_text_frame[i], text = "$17", font=("Conmic Sans MS","20","bold"), fg = "red", bg="linen"))
            self.gou_price_label[i].grid(row = 2, column = 1, sticky = W, pady = 20, padx = 40)

            self.gou_reduce_num_btn.append(Button(self.gou_product_text_frame[i], text = "-"))
            self.gou_reduce_num_btn[i].grid(row = 2, column = 1, sticky = E, pady = 20, padx = 100)

            self.gou_num_label.append(Label(self.gou_product_text_frame[i], text = "0"))
            self.gou_num_label[i].grid(row = 2, column = 1, sticky = E, pady = 20, padx = 68)
            
            self.gou_add_num_btn.append(Button(self.gou_product_text_frame[i], text = "+"))
            self.gou_add_num_btn[i].grid(row = 2, column = 1, sticky = E, pady = 20, padx = 40)   
            
            self.gou_add_cart_btn.append(Button(self.gou_product_text_frame[i], text = "ADD TO CART", fg = "red"))
            self.gou_add_cart_btn[i].grid(row = 3, column = 1, sticky = S, pady = 6, padx = 0)
            # i += 1

        
        
        


#main
if __name__ == '__main__':
    root = Tk()
    buttons = Main(root)
    root.title ("Heavenly Pizza GUI Ordering System")
    
    root.mainloop()

