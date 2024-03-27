class RNG:
    def __init__(self):
        try:
            numbers_file = open('numbers.txt','r')
            self.numbers = [int(x) for x in numbers_file.read()]
            numbers_file.close()
        except FileNotFoundError:
            self.numbers = []
            self.repopulate()
    def univariate(self,n=1):
        if n > 1000:
            raise Exception('RNG must be below 1000 digits')
        if len(self.numbers)<n:
            self.repopulate()
        numbers = self.numbers[:n]
        del self.numbers[:n]
        numbers_file = open('numbers.txt','w')
        numbers_file.write(''.join(map(str,self.numbers)))
        numbers_file.close()
        return numbers
    def repopulate(self):
        response = requests.get('https://qrng.anu.edu.au/API/jsonI.php?length=1024&type=hex16&size=1')
        file = open('numbers.txt','w')
        file.write(''.join([str(int(x,16)%2) for x in response.json()['data']]))
        file.close()
        self.numbers = [int(x,16)%2 for x in response.json()['data']]
    def uniform(self,a=0,b=1): #including a and b
        number_range = b-a
        bits = self.univariate(math.ceil(math.log2(number_range)))
        number = int(''.join(map(str,bits)),2)+a
        if number-a not in range(number_range+1): #rejection sampling
            number = uniform(self,a,b)
        return number
