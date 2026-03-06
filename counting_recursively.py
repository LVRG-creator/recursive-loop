def count_down(n):
    print(n)

    # print first, then decide if should keep going.

    if n == 0:
        # hit zero, no more counting down
        
        return
    # call again but with one less
    count_down(n - 1)
    
    #testing
if __name__ == "__main__":
    print("Counting down")
    count_down(5)