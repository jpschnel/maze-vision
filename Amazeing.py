import img_translator as it
import maze_vision_algo as mvsp
def main():
	rad = it.trans_main()
	print(rad)
	mvsp.mvsp(rad)
main()
