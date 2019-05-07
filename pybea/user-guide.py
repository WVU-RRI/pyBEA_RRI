# -*- coding: utf-8 -*-

#import pybea # pip install version
import pybea_rri as pybea # modified version

# Meta-Data API Methods
# The BEA API contains three methods for retrieving meta-data as follows:
#
# GetDataSetList: retrieves a list of the datasets currently offered.
# GetParameterList: retrieves a list of the parameters (required and optional) for a particular dataset.
# GetParameterValues: retrieves a list of the valid values for a particular parameter.
# Each of these methods has a corresponding function in the pybea package.

# Example Usage

# replace this with your BEA data API key!
USER_ID = 'AB044571-6562-46FA-814B-7DB0F4C56F96' # It's mine (Peter)

available_datasets = pybea.get_data_set_list(USER_ID)
print(available_datasets)

request1 = pybea.api.DataSetListRequest(USER_ID, ResultFormat="JSON")
print(request1.data_set_list)

regional_income_params = pybea.get_parameter_list(USER_ID, \
                                                  DataSetName='RegionalIncome', \
                                                  ResultFormat="XML")
print(regional_income_params)

request2 = pybea.api.ParameterListRequest(USER_ID, \
                                         DataSetName='RegionalIncome', \
                                         ResultFormat="JSON")
print(request2.parameter_list)

regional_income_geofips = pybea.get_parameter_values(USER_ID, \
                                                     DataSetName='RegionalIncome', \
                                                     ParameterName='GeoFips')
#print(regional_income_geofips)

request3 = pybea.api.ParameterValuesRequest(USER_ID, \
                                           DataSetName='RegionalIncome', \
                                           ParameterName='GeoFips')
#print(request3.parameter_values)

# Data Retrieval API Method
# The BEA API has one method for retrieving data: GetData. 
# This method has its own function in the pybea package.

# NIPA (National Income and Product Accounts)
# This dataset contains data from the National Income and Product Accounts which include 
# measures of the value and composition of U.S.production and the incomes generated in producing it. 
# NIPA data is provided on a table basis; individual tables contain between fewer than 10 to more 
# than 200 distinct data series.

# Example Usage
# Percent change in Real Gross Domestic Product, Annually and Quarterly for all years.
data1 = pybea.get_data(USER_ID, DataSetName='NIPA', TableName='T10101', \
                      Frequency=['A', 'Q'], Year='ALL', ResultFormat="XML")
print( data1.head() )
print( data1.tail() )

# Example Usage
# Personal Income, Monthly, for 2015 and 2016.

request4 = pybea.api.NIPARequest(USER_ID, TableName='T20600', Frequency='M', \
                                Year=['2015', '2016'], ResultFormat='JSON')
print( request4.data.head() )
print( request4.data.tail() )
data_of_request4 = request4.data

# NIUnderlyingDetail (National Income and Product Accounts)

# Example Usage
# Personal Consumption Expenditures, Current Dollars, Annually, Quarterly and Monthly for all years.
data2 = pybea.get_data(USER_ID, DataSetName='NIUnderlyingDetail', TableName='U20305', \
                      Frequency=['A', 'Q'], Year='ALL', ResultFormat='XML')
print( data2.head() )
print( data2.tail() )

#Example Usage
#Auto and Truck Unit Sales, Production, Inventories, Expenditures and Price, Monthly, for 2015 and 2016
request5 = pybea.api.NIUnderlyingDetailRequest(USER_ID, TableName='U70205S', Frequency='M', \
                                              Year=['2015', '2016'], ResultFormat='JSON')
print( request5.data.head() )
print( request5.data.tail() )
data_of_request5 = request5.data

#ITA (International Transactions)

#Example Usage
#Balance on goods with China for 2011 and 2012.
data3 = pybea.get_data(USER_ID, DataSetName='ITA', Indicator='BalGds', AreaOrCountry='China', \
                      Frequency='A', Year=['2011', '2012'], ResultFormat='XML')
print( data3.head() )

# Example Usage
# Net U.S. acquisition of portfolio investment assets (quarterly not seasonally adjusted) for 2013.
data4 = pybea.get_data(USER_ID, DataSetName='ITA', Indicator='PfInvAssets', AreaOrCountry='AllCountries', \
                      Frequency='QNSA', Year='2013', ResultFormat='XML')
print( data4.head() )

# Regional Income

# Example Usage
# Fetch data on personal income for 2012 and 2013 for all counties, in JSON format
data5 = pybea.get_data(USER_ID, DataSetName='RegionalIncome', TableName='CA1', LineCode=1, \
                      GeoFips='COUNTY', Year=['2012', '2013'], ResultFormat='JSON')
print( data5.head() )
print( data5.tail() )


# Fixed Assets
# The FixedAssets dataset contains data from the standard set of Fixed Assets tables as published online.
#data6 = pybea.get_data(USER_ID, DataSetName='FixedAssets', TableID='16', Year='2012', ResultFormat='XML')
#print( data6.head() )
#print( data6.tail() )

# RegionalProduct
# Example Usage
# Real GDP for all years for all MSAs, in JSON format
data6 = pybea.get_data(USER_ID, DataSetName='RegionalProduct', Component="RGDP_MAN", IndustryId=1, \
                       GeoFips="MSA", Year="ALL", ResultFormat='JSON')
data7 = pybea.get_data(USER_ID, DataSetName='RegionalProduct', Component="GDP_SAN", IndustryId=1, \
                       GeoFips="STATE", Year="ALL", ResultFormat='JSON')
print( data6.head() )
print( data6.tail() )
print( data7.head() )
print( data7.tail() )

# Example Usage
# GDP for 2012 and 2013 for selected Southeast states, for the Retail Trade industry.
#southeast_states = ["01000", "05000", "12000", "13000", "21000", "22000", 
#                    "28000", "37000", "45000", "47000", "51000", "54000"]
#data8 = pybea.get_data(USER_ID, DataSetName='RegionalProduct', Component="GDP_sAN", IndustryId=35, \
#                      GeoFips=southeast_states, Year=["2013", "2013"], ResultFormat='XML')
#print( data8.head() )
#print( data8.tail() )

# Input Output

# Example Usage
# Data from The Use of Commodities by Industries, Before Redefinitions (Producer’s Prices) 
# sector level table for years 2010, 2011, and 2012.
#data9 = pybea.get_data(USER_ID, DataSetName='InputOutput', TableID=2, \
#                      Year=['2010', '2011', '2012', '2013'], ResultFormat='JSON')
#print( data9.head() )
#print( data9.tail() )

# Example Usage
# Data for 2007 from The Make of Commodities by Industries, Before Redefinitions sector and 
# summary level tables.
#data10 = pybea.get_data(USER_ID, DataSetName='InputOutput', TableID=[46, 47], \
#                      Year='2007', ResultFormat='JSON')
#print( data10.head() )
#print( data10.tail() )
