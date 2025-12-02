def trap(height):
    water = l = 0
    r = len(height)-1
    lmax = height[0]
    rmax = height[len(height)-1]
    while l<r:
        if height[l]<height[r]:
            if height[l]>lmax:
                lmax = height[l]
            else:
                water += lmax - height[l]
            l+=1
        else:
            if height[r]>rmax:
                rmax = height[r]
            else:
                water += rmax - height[r]
            r-=1
    return water

#main
height = list(map(int, input("Enter height values:").split()))
print(trap(height))