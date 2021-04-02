# Simple pygame program

# Import and initialize the pygame library
import pygame
import pygame.gfxdraw
import math
import subprocess

# Find screen resolution
cmd = ['xrandr']
cmd2 = ['grep', '*']
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)
p.stdout.close()
resolution_string, junk = p2.communicate()
resolution = resolution_string.split()[0]
resolution = resolution.decode('utf-8')
width, height = resolution.split('x')
width = int(width)
depth = int(height)

# Initialize pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([width, depth])
screen_size = pygame.Surface.get_size(screen)

# Assign global variables
PI = math.pi
black = (0, 20, 20)
blue = (0, 190, 160)
bluer = (0, 60, 50)
center = (int(screen_size[0]/2), int(screen_size[1]/2))
cx = center[0]
cy = center[1]
cxy = 0
if cx < cy:
    cxy = cx
else:
    cxy = cy

altl = 50
altr = 150
altw = 2

# Define function to pass radius and return square dimensions
def sq_call(r):
    square = [(cx - r), (cy - r), 2*r, 2*r]
    return square

def rad(deg):
    radians = deg*PI/180
    return radians

def apu(radius, begin_deg, end_deg, depth, outline):
    pygame.draw.arc(screen, blue, sq_call(radius), rad(begin_deg), rad(end_deg), depth)
    
    if begin_deg >= 90 and begin_deg < 270:
        mid_deg = begin_deg + int((end_deg - begin_deg)*.6)
        pygame.draw.arc(screen, blue, sq_call(int(radius*1.07)), rad(begin_deg), rad(mid_deg), int(depth/2))
        pygame.draw.arc(screen, blue, sq_call(int(radius*1.07)), rad(begin_deg+outline), rad(mid_deg-outline), int(depth/2))
    else:
        mid_deg = end_deg - int((end_deg - begin_deg)*.6)
        pygame.draw.arc(screen, blue, sq_call(int(radius*1.07)), rad(mid_deg), rad(end_deg), int(depth/2))
        pygame.draw.arc(screen, blue, sq_call(int(radius*1.07)), rad(begin_deg+outline), rad(mid_deg-outline), int(depth/2))
        
    pygame.draw.arc(screen, black, sq_call(radius-5), rad(begin_deg+outline), rad(end_deg-outline), depth-outline)

# Define a main loop
def main():
    running = True
    j = 0
    k = 0
    l = 0
    m = 0
    
    #Draw on the screen
    def redraw():
        box = 0
        
        # Fill the background with white
        screen.fill((0, 20, 20))

        # Add box modules
        while (box < depth-250):
            pygame.draw.polygon(screen, blue, [(width - 400, box + 230), (width - 400, box + 86), (width - 350, box + 40), (width - 100, box + 40), (width - 100, box + 230)], 5)
            
            box += 250
        
        # Draw grid on background
        for i in range(25, width, 50):
            pygame.draw.line(screen, bluer, (i, 0), (i, depth))
        for i in range(25, depth, 50):
            pygame.draw.line(screen, bluer, (0, i), (width, i))
        
        for i in range(125, width, 250):
            pygame.draw.line(screen, bluer, (i, 0), (i, depth), 3)
        for i in range(125, depth, 250):
            pygame.draw.line(screen, bluer, (0, i), (width, i), 3)
        
        # Draw Altimeter lines in the top left
        for i in range(50, 350, 30):
            endy = i+l
            start = (altl, endy)
            end = (altr, endy)
            pygame.draw.line(screen, blue, start, end, altw)
        pygame.draw.line(screen, blue, (altl-10, 50+m), (altr+10, 50+m), altw*4)
        
        # Draw an arc reactor in the center
        pygame.draw.circle(screen, black, center, 200)
        pygame.draw.circle(screen, blue, center, 195, 10)
        pygame.draw.circle(screen, blue, center, 125, 10)
        pygame.draw.circle(screen, blue, center, 110)
        pygame.draw.circle(screen, black, center, 75, 3)
        pygame.draw.circle(screen, black, center, 55, 3)
        pygame.draw.circle(screen, black, center, 35, 3)
        
        for i in range(3, 43, 4):
            pygame.draw.arc(screen, (0, 190, 160), sq_call(180), (i+k)*PI/20, (i+k+2)*PI/20, 50)
        
        for i in range(3, 86, 4):
            pygame.draw.arc(screen, (0, 20, 20), sq_call(100), (i+j)*PI/40, (i+j+2)*PI/40, 20)
        for i in range(1, 43, 14):
            pygame.draw.arc(screen, (0, 20, 20), sq_call(125), (i+5)*PI/20, (i+7)*PI/20, 50)
        
        # Add pie-piece pop-out to the arc reactor
        #apu(505, 140, 120, 430, 2)
        pygame.draw.arc(screen, blue, sq_call(505), rad(140), rad(200), 430)
        pygame.draw.arc(screen, blue, sq_call(535), rad(140), rad(170), 50)
        pygame.draw.arc(screen, black, sq_call(500), rad(141), rad(198), 427)
        pygame.draw.arc(screen, black, sq_call(530), rad(141), rad(168), 50)
        
        # Add another pie-piece pop-out to the arc reactor
        #pygame.draw.arc(screen, blue, sq_call(505), rad(300), rad(340), 430)
        #pygame.draw.arc(screen, blue, sq_call(535), rad(140), rad(170), 50)
        #pygame.draw.arc(screen, black, sq_call(500), rad(301), rad(339), 427)
        #pygame.draw.arc(screen, black, sq_call(530), rad(141), rad(168), 50)
        

        
        # Update the display
        pygame.display.flip()
        
    # Run until the user asks to quit
    while running:
        # Assign variables for framerates
        j += -.001
        k += .01
        if l < 30:
            l += .2
        else:
            l = 0
            
        if m < 300:
            m += .2
        else:
            m = 0
        
        # Call the new version of the drawing
        redraw()
        
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Done! Time to quit.
    pygame.quit()


main()
