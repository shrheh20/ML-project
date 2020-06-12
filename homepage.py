choice = 0
while choice !=4:
    choice = int(input("\n\n******Enter Choice:******\n 1.Clustering\n 2.SVM\n 3.KNN\n 4.Exit\n"))
    if choice == 1:
        import Clustering
   
    elif choice == 2:
        import SVM_FINAL_DRAFT
  
    elif choice == 3:
        import KNN

    elif choice == 4:
        pass
   
    else:
        print("Enter Valid Choice!")
    
