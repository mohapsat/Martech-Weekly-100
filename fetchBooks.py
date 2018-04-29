from amazon.api import AmazonAPI
import idx_config as conf
from algoliasearch import algoliasearch
import json


amazon = AmazonAPI(conf.AMAZON_ACCESS_KEY, conf.AMAZON_SECRET_KEY, conf.AMAZON_ASSOC_TAG)

# bn = amazon.browse_node_lookup(BrowseNodeId=1000)
#
# print(bn.)

products = amazon.search_n(1000
                           , Keywords="marketing technology"
                           , SearchIndex='Books'
                           # , ResponseGroup='TopSellers'
                           , Sort='relevancerank')

# Valid response groups for ItemLookup requests include ['Request','ItemIds','Small','Medium','Large','Offers','OfferFull','OfferSummary','OfferListings','PromotionSummary','PromotionDetails','VariationMinimum','VariationSummary','VariationMatrix','VariationOffers','Variations','TagsSummary','Tags','ItemAttributes','MerchantItemAttributes','Tracks','Accessories','EditorialReview','SalesRank','BrowseNodes','Images','Similarities','Subjects','Reviews','ListmaniaLists','SearchInside','PromotionalTag','SearchBins','AlternateVersions','Collections','RelatedItems','ShippingCharges','ShippingOptions'].'

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
    data[i] = {
                       "title" : str(product.title)[0:90]
                      ,"sales_rank" : str(product.sales_rank)
                      ,"author" : str(product.author)[0:20]
                      ,"large_image_url" : product.large_image_url
                      ,"publisher" : str(product.publisher)[0:34]
                      ,"publication_date" : str(product.publication_date)
                      ,"detail_page_url" : product.detail_page_url
                      ,"asin" : str(product.asin)
                      ,"availability" : str(product.availability)[0:25]
                      ,"isbn" : str(product.isbn)
                      ,"offer_url" : product.offer_url
                      ,"pages" : str(product.pages)
                      ,"price_and_currency" : str(product.price_and_currency[0])
                      ,"list_price" : str(product.list_price[0])
                      ,"binding" : str(product.binding)[0:25]
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
#trunc and load index
index.clear_index()

#load index
batch = json.load(open('mt101_data.txt'))
# # #
# # # # add json to index idx_mt101
index.add_objects(batch)
#
#











