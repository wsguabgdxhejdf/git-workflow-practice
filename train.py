for epoch in range(5):
    loss = 1 / (epoch + 1)
    print(f"epoch={epoch}, loss={loss}")
    
print("training finished")