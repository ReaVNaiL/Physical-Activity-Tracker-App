# 
# {
#   "summary": object,
#   "averages_section": AverageModel,
#   "user_data_details": UserDataDetailsModel,
# }
# 

from dataclasses import dataclass
import AveragesModel as avg
import UserDataDetailsModel as uddm


@dataclass
class DashboardSummaryModel:
        averages_section: avg.AveragesModel
        summary: object = None
        user_data_details: uddm.UserDataDetailsModel = None
        
        
# """ Demo Code """

# # Generic Object
# Object = lambda **kwargs: type("Object", (), kwargs)()

# # Create summary object empty // Might avoid this
# summary = Object(name = "summary")

# # Demo data
# average = avg.AveragesModel(ACC=1.0, EDA=2.0, Temp=3.0)

# # Create DashboardSummaryModel object
# new_dash = DashboardSummaryModel(average, summary, None)
# print(new_dash.summary.name)