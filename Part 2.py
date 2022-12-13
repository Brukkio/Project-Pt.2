# Bruk Tewelde:1834503 Project Part 2

import csv

import datetime


#  class primarily to process specified files

class ProcessFile:

    # constructor to recognize and read all directed input files

    def __init__(self, manufactureListFile, priceListFile, serviceDatesFile):

        #  the specific dictionaries for all the files

        self.product = {}

        self.priceList = {}

        self.serviceDate = {}

        #  primary functions to read all the specified files

        self._read_manufactureList(manufactureListFile)

        self._readPriceList(priceListFile)

        self._readServiceDates(serviceDatesFile)

    # primary function to read the manufacturer list

    def _read_manufactureList(self, filename):

        with open(filename) as f:

            csvreader = csv.reader(f)

            # when using csv reader, it reads the file, then adds it into the dictionary

            for row in csvreader:

                _id = row[0]

                name = row[1]

                _type = row[2]

                self.product[_id] = {}

                self.product[_id]['Name'] = name

                self.product[_id]['Type'] = _type

                if len(row) > 3:
                    self.product[_id]['Damaged'] = row[3]

    # read-file functionality for price lists

    def _readPriceList(self, filename):

        with open(filename) as f:
            csvreader = csv.reader(f)

            # utilizing csv reader to access the dictionary file

            for row in csvreader:
                _id = row[0]

                price = row[1]

                self.priceList[_id] = float(price)

    # main mechanism to acquire the file's service date list

    def _readServiceDates(self, filename):

        with open(filename) as f:
            # utilizing csv reader to access the dictionary file

            csvreader = csv.reader(f)

            for row in csvreader:
                _id = row[0]

                date = row[1]

                # converts date in data time

                self.serviceDate[_id] = datetime.datetime.strptime(date, "%m/%d/%Y")

    # primary operation for the query to process

    def Query(self, query):

        products = []

        # read the dictionary

        for key, values in self.product.items():

            # examine the product list to see if the name and type are there; if not, return.

            if values['Name'].strip() + ' ' + values['Type'].strip() in query:
                products.append(key)

        if not products:
            print("No such item in inventory")

            return

        expensive_product = 0

        expensive_product_id = None

        current = datetime.datetime.now()

        # choose the most expensive item from the product goods that is in excellent condition and hasn't expired.

        for product in products:

            if self.product[product]['Damaged'] == '' and self.serviceDate[product] > current:

                if self.priceList[product] > expensive_product:
                    expensive_product_id = product

                    expensive_product = self.priceList[product]

        # Print item details

        if expensive_product_id:
            print(
                f"Your item is: Id: {expensive_product_id} Manufacturer Name: {self.product[expensive_product_id]['Name']} Item type: {self.product[expensive_product_id]['Type']} Price: {expensive_product}")

        similar_item = None

        similar_item_dif = float('-inf')

        #  verify comparable items with the lowest price that are not damaged or expired.

        itemtype = self.product[expensive_product_id]['Type']

        for key, values in self.product.items():

            if key != expensive_product_id:

                if values['Type'] == itemtype:

                    if values['Damaged'] == '' and self.serviceDate[key] > current:

                        dif = abs(self.priceList[key] - expensive_product)

                        if dif > similar_item_dif:
                            similar_item = key

        # print the identicle items if they are present.

        if similar_item:
            print(
                f"You may also consider : Id: {similar_item} Manufacturer Name: {self.product[similar_item]['Name']} Item type: {self.product[similar_item]['Type']} Price: {self.priceList[similar_item]}")

    # Section for the search function/query

    def search(self):

        while True:

            # recieve the query

            query = input('Enter your query: ')

            # processing the query

            self.Query(query)

            # verify if the selected user wants to continue

            choice = input("Enter q to quit : ")

            if choice == 'q':
                break


# Process files

data = ProcessFile('ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv')

# Input and or enter the search interface.

data.search()