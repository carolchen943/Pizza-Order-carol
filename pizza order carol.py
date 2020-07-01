from tkinter import *

class Main:
    def __init__(self, parent):
        
        WIDTH = 1366
        HEIGHT = 768
        num_cols = 4
        num_rows = 2
        global images
        global gou_images
        
        regular_name = [
            'Margherita', 'Kiwi', 'Garlic', 'Cheese', 'Hawaiian', 'Mediterranean (vegan)'
        ]
        regular_img = [
            'img/Margherita.gif', 'img/Kiwi.gif', 'img/Garlic.gif', 'img/Cheese.gif',
            'img/Hawaiian.gif', 'img/Mediterranean (vegan).gif'
        ]
        regular_content = [
            'Fresh tomato, mozzarella, fresh basil, parmesan', 'Bacon, egg, mozzarella',
            'Mozzarella, garlic', 'Mozzarella, oregano',
            'Ham, pineapple, mozzarella', 'Lebanese herbs, olive oil, fresh tomatoes, olives, onion'
        ]
        gourment_name = [
            'Meat', 'Chicken Cranberry', 'Satay Chicken', 'Big BBQ Bacon', 'Veggie', 'Meatlovers'
        ]
        gourment_img = [
            'img/Margherita.gif', 'img/Kiwi.gif', 'img/Garlic.gif', 'img/Cheese.gif',
            'img/Hawaiian.gif', 'img/Mediterranean (vegan).gif'
        ]
        gourment_content = [
            'Bacon, pancetta, ham, onion, pepperoni, mozzarella', 'Smoked chicken, cranberry, camembert mozzarella',
            'Smoked chic, onions, capsicum, pine nuts, satay sauce, mozzarella Chilli flakes and dried basil',
            'Smoky Bacon served on our classic marinara tomato sauce, heaped with mozzarella, topped off with a sweet and tangy BBQ drizzle', 
            'sweet red onion, mushroom, red capsicum & melting mozzarella with drizzles of our tangy roast capsicum drizzle, finished with a dash of oregano',
            'Spicy pepperoni, Italian sausage, succulent ham, seasoned ground beef and crispy bacon all piled onto classic marinara sauce and finished with cheesy mozzarella and a drizzle of BBQ'
        ]


        #top menu frame
        self.frame1 = Frame(parent, bg="linen", padx=30, height = 30)
        self.frame1.grid(row = 0, columnspan = 7)
        #welcome label
        welcome_label = Label(self.frame1, text = "Welcome, ", bg = "linen")
        welcome_label.grid(row=0, column=0, sticky = W, padx = 3)
        #logout button
        logout_btn = Button(self.frame1, text = "Log out", bg = "linen")
        logout_btn.grid(row=0, column=1, sticky = W, pady = 1)
        #regular pizza menu button
        regular_btn = Button(self.frame1, text = "Regular pizzas ", bg = "linen", command = self.regular)
        regular_btn.grid(row=0, column=2, sticky = W, pady = 1)
        #gourmet pizza menu button
        gourmet_btn = Button(self.frame1, text = "Gourmet pizzas", bg = "linen", command = self.gourment)
        gourmet_btn.grid(row=0, column=3, sticky = W, pady = 1)
        #check out button
        checkout_btn = Button(self.frame1, text = "Checkout", bg = "linen")
        checkout_btn.grid(row=0, column=4, sticky = W, pady = 1)
        #cart button
        cart_btn = Button(self.frame1, text = "CART", bg = "linen")
        cart_btn.grid(row=0, column=5, sticky = W, pady = 1)
        #total button
        total_label = Label(self.frame1, text = "Total = ", bg = "linen")
        total_label.grid(row=0, column=6, sticky = W, pady = 1)

    
        #regular frame        
        self.frame2 = Frame(parent, bg="linen", width = WIDTH, height = 500)
        self.frame2.grid(row = 1, columnspan = 4)
        #product frame
        self.re_product_frame = []
        for i in range(len(regular_name)):
            self.re_product_frame.append(Frame(self.frame2, bg="linen", width = WIDTH, height = 50))
        frame_count = 0
        for c in range(num_cols):
            for r in range(num_rows):
                if frame_count < len(regular_name):
                    self.re_product_frame[frame_count].grid(row = r, column = c)
                    frame_count += 1
        #names and images of each regular pizza
        self.re_name_label = []
        self.re_img_label = []
        self.re_content_label = []
        self.re_add_cart_btn = []
        i = 0

        images = []
        for r in regular_img:
            images.append(PhotoImage(file = r))
        # print(images)
        for i in range(len(regular_name)):
            #print(i, len(self.product_frame), regular_name,images[i])
            self.re_name_label.append(Label(self.re_product_frame[i], text = regular_name[i]))
            self.re_name_label[i].grid(row = 0, column = 0, sticky = N+W+S+E, pady = 5)

            self.re_img_label.append(Label(self.re_product_frame[i], image=images[i]))
            self.re_img_label[i].grid(row = 1, column = 0)
            
            self.re_content_label.append(Label(self.re_product_frame[i], text = regular_content[i]))
            self.re_content_label[i].grid(row = 2, column = 0, sticky = N+W+S+E, pady = 3)

            self.re_add_cart_btn.append(Button(self.re_product_frame[i], text = "ADD TO CART", fg = "red"))
            self.re_add_cart_btn[i].grid(row = 3, column = 0, sticky = N+W+S+E, pady = 1)
            i += 1


#########gourment part###########
        #create gourment frame
        self.gourment_frame = Frame(parent, bg="linen", width = WIDTH, height = 500)
        ##self.gourment_frame.grid(row = 0, columnspan = 3)        

        #create gourment pizza product frames
        gou_num_cols = 3
        gou_num_rows = 6
        self.gou_product_frame = []

        self.gou_name_label = []
        self.gou_img_label = []
        self.gou_content_label = []
        self.gou_add_cart_btn = []
        i = 0
        #create gourment pizza images list
        gou_images = []
        for r in gourment_img:
            gou_images.append(PhotoImage(file = r))
        #divide the whole big gourment frame into 6*3 small product frames, with the arrangment of the first column is used to display images,
        #the second is used to display labels(names, contents) and add-to-cart button, the third column is totally empty.
        #I'm planning to define the width and height of the first and the second column.
        frame_count = 0
        for r in range(gou_num_rows):
            # for c in range(gou_num_cols):
                # if frame_count < (len(gourment_name))*3: #loop 6*3 times, since there are 6*3 grids in total
            # if c == 0: #At first column, I'm planning to add images, with width and height setted. 
            self.gou_product_frame.append(Frame(self.gourment_frame, bg="linen", width = 881, height = 300))
            self.gou_product_frame[r].grid(row = r, column = 0)
            self.gou_product_frame[r].grid_propagate(0)
                
            # elif c == 1: #At second column, I'm planning to add labels&button(name,content, add-to-cart button), with width and height setted.
            #     self.gou_product_frame.append(Frame(self.gourment_frame, bg="linen", width = 100, height = 50))
            #     self.gou_product_frame[frame_count].grid(row = r, column = c)
            #     self.gou_product_frame[frame_count].grid_propagate(0)
                
            # else:  #refers to the third column, which have nothing in them, so no width and height needed.
            #     self.gou_product_frame.append(Frame(self.gourment_frame, bg="linen"))
            #     self.gou_product_frame[frame_count].grid(row = r, column = c)
                                           
            #         # frame_count += 1

        #the names,images, add-to-cart buttons of each gourment pizza in each gourment product frame
        for i in range(len(gourment_name)):
            #print(i, len(self.product_frame), regular_name,images[i])

            self.gou_img_label.append(Label(self.gou_product_frame[i], image=gou_images[i]))
            self.gou_img_label[i].grid(row = 0, column = 0)

            self.gou_name_label.append(Label(self.gou_product_frame[i], text = gourment_name[i]))
            self.gou_name_label[i].grid(row = 0, column = 1, sticky = N, pady = 5)
            
            self.gou_content_label.append(Label(self.gou_product_frame[i], text = gourment_content[i]))
            self.gou_content_label[i].grid(row = 0, column = 2, sticky = S, pady = 3)

            self.gou_add_cart_btn.append(Button(self.gou_product_frame[i], text = "ADD TO CART", fg = "red"))
            self.gou_add_cart_btn[i].grid(row = 0, column = 3, sticky = S, pady = 1)
            # i += 1

    def regular(self):
        self.gourment_frame.grid_forget()
        self.frame2.grid(row = 1, columnspan = 4) 

    def gourment(self):
        self.frame2.grid_forget()
        self.gourment_frame.grid(row = 1, columnspan = 3)   


#main
if __name__ == '__main__':
    root = Tk()
    buttons = Main(root)
    root.title ("Heavenly Pizza GUI Ordering System")
    root.mainloop()
