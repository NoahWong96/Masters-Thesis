
def main1():


  rangex = [-5, 5]
  rangey = [-5, 5]

  dx = 0.001
  dy = 0.001

  distanceX = rangex[1] - rangex[0]
  distanceY = rangey[1] - rangey[0]

  datapointsX = distanceX/ dx
  datapointsY = distanceY/dy

  datapoints = datapointsX * datapointsY

  a = 0
  b = 0

  print(iterFunction(0,0,1,0))



def iterFunction(a,b,x,y):
    numeratorX = a * (1 + x^2 - y^2) - 2*x*(1- b*y + x^2 + y^2)
    numeratorY = b * (1 + x^2 - y^2) - 2*y*(-1+a*x + x^2 + y^2)
    denominator = a^2 + b^2 - 4*(x^2 + y^2)

    if denominator ==0:
        return "infty"

    else:
        return [numeratorX/denominator, numeratorY/denominator]


if __name__ == '__main__':
    main1()
