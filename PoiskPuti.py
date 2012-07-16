###################
#mode(on keyboard):
#0) passive
#1) create road
#2) create wall
#3) delete
#4) delete 9 cells
###################
#Press S to save map
###################
import time
import string
import pygame
import pickle

pygame.init()

def main():
	screen_size = 640, 640
	screen = pygame.display.set_mode(screen_size, pygame.DOUBLEBUF | pygame.HWSURFACE)
	
	done=False
	
	file=open('base_new.txt','r')
	roads=pickle.load(file)
	walls=pickle.load(file)
	file.close
	
	i=0	
	mode=0
	
	print 'walls :' 
	print walls
	print 'roads :' 
	print roads
	
	zoom = 10
	pos=0,0
	
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done=True
			if event.type == pygame.MOUSEMOTION:
				pos=event.pos[0]/zoom*zoom,event.pos[1]/zoom*zoom,
				if mode==1:
					x=pos[0]/zoom
					y=pos[1]/zoom
					
					i=0					
					while i<len(walls):						
						if walls[i]==[x,y]:
							walls.pop(i)
						i+=1
					
					j=0
					dubl=False					
					while j<len(roads):						
						if roads[j]==[x,y]:
							dubl=True
						j+=1
					if not dubl:
						roads.append([x,y])		
				if mode==2:
					x=pos[0]/zoom
					y=pos[1]/zoom
					
					i=0					
					while i<len(roads):						
						if roads[i]==[x,y]:
							roads.pop(i)
						i+=1
					
					j=0
					dubl=False					
					while j<len(walls):						
						if walls[j]==[x,y]:
							dubl=True
						j+=1
					if not dubl:
						walls.append([x,y])	
						
				if mode==3:
					x=pos[0]/zoom
					y=pos[1]/zoom
					
					i=0					
					while i<len(roads):						
						if roads[i]==[x,y]:
							roads.pop(i)						
						i+=1
					
					i=0					
					while i<len(walls):						
						if walls[i]==[x,y]:
							walls.pop(i)
						i+=1
				if mode ==4:
					x=pos[0]/zoom
					y=pos[1]/zoom
					
					i=0					
					while i<len(roads):						
						if roads[i]==[x,y]:
							roads.pop(i)
						if i<len(roads):
							if roads[i]==[x-1,y]:
								roads.pop(i)
						if i<len(roads):
							if roads[i]==[x,y-1]:
								roads.pop(i)
						if i<len(roads):
							if roads[i]==[x-1,y-1]:
								roads.pop(i)
						if i<len(roads):
							if roads[i]==[x+1,y]:
								roads.pop(i)
						if i<len(roads):
							if roads[i]==[x,y+1]:
								roads.pop(i)
						if i<len(roads):
							if roads[i]==[x+1,y+1]:
								roads.pop(i)
						if i<len(roads):
							if roads[i]==[x+1,y-1]:
								roads.pop(i)
						if i<len(roads):
							if roads[i]==[x-1,y+1]:
								roads.pop(i)
						i+=1
					
					i=0					
					while i<len(walls):						
						if walls[i]==[x,y]:
							walls.pop(i)
						if i<len(walls):
							if walls[i]==[x-1,y]:
								walls.pop(i)
						if i<len(walls):
							if walls[i]==[x,y-1]:
								walls.pop(i)
						if i<len(walls):
							if walls[i]==[x-1,y-1]:
								walls.pop(i)
						if i<len(walls):
							if walls[i]==[x+1,y]:
								walls.pop(i)
						if i<len(walls):
							if walls[i]==[x,y+1]:
								walls.pop(i)
						if i<len(walls):
							if walls[i]==[x+1,y+1]:
								walls.pop(i)
						if i<len(walls):
							if walls[i]==[x+1,y-1]:
								walls.pop(i)
						if i<len(walls):		
							if walls[i]==[x-1,y+1]:
								walls.pop(i)
						i+=1
				
			if event.type == 5:
				if event.button == 4:#+
					if zoom<=100:
						zoom*=2					
				if event.button == 5:#-
					if zoom>=5:
						zoom/=2
						
			if event.type == pygame.KEYDOWN:	
				if event.key == 48:#0_passive
					mode=0
				if event.key == 49:#1_add_road
					mode=1					
				if event.key == 50:#2_add_wall
					mode=2
				if event.key == 51:#3_del
					mode=3
				if event.key == 52:#4_hard_del
					mode=4
				if event.key == 115:#s_save
					file=open('base_new.txt','w')
					pickle.dump(roads, file)
					pickle.dump(walls, file)
					file.close
					print 'save completed'
				if event.key == 99:#c_create - nomer lvla vvodim ru4kami tut=\
					file=open('main_base.txt','w')
					roads_level_=roads
					walls_level_=walls
					pickle.dump(roads_level_, file)
					pickle.dump(walls_level_, file)
					file.close
					print 'save level competed'
		#render
			screen.fill((255, 255, 255))
			
			i=0
			while i<len(walls):
				pygame.draw.rect(screen,(128,128,128),(walls[i][0]*zoom,walls[i][1]*zoom,zoom,zoom))
				i+=1
				
			i=0
			while i<len(roads):
				pygame.draw.rect(screen,(127,255,0),(roads[i][0]*zoom,roads[i][1]*zoom,zoom,zoom))
				i+=1
			if mode==1 or mode==2 or mode==3:#little cell 
				pygame.draw.rect(screen,(100,100,100),(pos[0],pos[1],zoom,zoom))
			if mode==4:#big cell
				pygame.draw.rect(screen,(100,100,100),(pos[0]-zoom,pos[1]-zoom,zoom*3,zoom*3))
			pygame.display.flip()
		time.sleep(0.01)
main()