from tkinter import *
#from PIL import ImageTk, Image
class Main:
    def __init__(self, parent):
        
        WIDTH = 1366
        HEIGHT = 768
        num_cols = 3
        num_rows = 2
        global images
        
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


        #create the header frame
        self.frame1 = Frame(parent, bg="linen", padx=30, height = 30)
        self.frame1.grid(row = 0, columnspan = 7)
        #welcome label
        welcome_label = Label(self.frame1, text = "Welcome, ", bg = "linen")
        welcome_label.grid(row=0, column=0, sticky = W, padx = 3)
        #logout button
        logout_btn = Button(self.frame1, text = "Log out", bg = "linen")
        logout_btn.grid(row=0, column=1, sticky = W, pady = 1)
        #regular pizza menu button
        regular_btn = Button(self.frame1, text = "Regular pizzas ", bg = "linen")
        regular_btn.grid(row=0, column=2, sticky = W, pady = 1)
        #gourmet pizza menu button
        gourmet_btn = Button(self.frame1, text = "Gourmet pizzas", bg = "linen")
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
    
   
          


#main
if __name__ == '__main__':
    root = Tk()
    buttons = Main(root)
    root.title ("Heavenly Pizza GUI Ordering System")
    root.mainloop()
