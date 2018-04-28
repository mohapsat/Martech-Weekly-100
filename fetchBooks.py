from amazon.api import AmazonAPI
import idx_config as conf
from algoliasearch import algoliasearch
import json


amazon = AmazonAPI(conf.AMAZON_ACCESS_KEY, conf.AMAZON_SECRET_KEY, conf.AMAZON_ASSOC_TAG)

# bn = amazon.browse_node_lookup(BrowseNodeId=1000)
#
# print(bn.)

products = amazon.search_n(100
                           , Keywords='Marketing'
                           , SearchIndex='Books'
                           , ResponseGRoup='TopSellers'
                           , Sort='salesrank')
# Valid sort values include
#   'relevancerank'
# ,'salesrank'
# ,'reviewrank'
# ,'pricerank'
# ,'inverse-pricerank'
# ,'daterank'
# ,'titlerank'
# ,'-titlerank'
# ,'-unit-sales'
# ,'price'
# ,'-price'
# ,'-publication_date'.'

# make products json serializable
# response = json.dumps(products, default=lambda o: o.__dict__)


# print(products[0].title)

data = {}

# for i, product in enumerate(products):
#     mydict.update({i:product.title})
    # print("{0}. '{1}'".format(i, product.title))


for i, product in enumerate(products):
    data[i] = {"title" : product.title
                      ,"sales_rank" : str(product.sales_rank)
                      ,"author" : product.author
                      ,"large_image_url" : product.large_image_url
                      ,"publisher" : product.publisher
                      ,"publication_date" : str(product.publication_date)
                      ,"detail_page_url" : product.detail_page_url
                      ,"asin" : str(product.asin)
                      ,"availability" : product.availability
                      ,"isbn" : str(product.isbn)
                      ,"offer_url" : product.offer_url
                      ,"pages" : str(product.pages)
                      ,"price_and_currency" : str(product.price_and_currency[0])
                      ,"list_price" : str(product.list_price[0])
                      ,"binding" : product.binding
                   }

    # print("{0}. '{1}'".format(i, product.title))
data_list = list(data.values())
# print(data_list)

# json dump mydict and store in mydict_json
# data_json = json.dumps(data_list)
# #
# print(data_json)
#
# with open('mt101_data.json', 'w') as outfile: #will delete the old file an create a new one.
#     json.dumps(data_json, outfile)

with open('mt101_data.txt', 'w', encoding='utf-8') as f:
  json.dump(data_list, f, ensure_ascii=False)

################### Algolia #################
# ApplicationID = '***'
# ApiKey = '***'
client = algoliasearch.Client(conf.ApplicationID, conf.ApiKey)
# # #
index = client.init_index("idx_mt101")
# # #
batch = json.load(open('mt101_data.txt'))
# # #
# # # # add json to index idx_mt101
index.add_objects(batch)
#
#











