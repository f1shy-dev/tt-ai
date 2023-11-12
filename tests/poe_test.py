# from ttai_farm.analysis import PoeAnalysisProvider
# from ttai_farm.console import console
# farm = PoeAnalysisProvider(
#     bot_name="chinchilla", poe_api_token="")
# data = farm.analyze("""[0:00:00.000 --> 0:00:02.620] The Joe Rogan Experience.
# [0:00:02.900 --> 0:00:06.280] But I want to talk about chat GPT.
# [0:00:06.900 --> 0:00:07.360] Hmm.
# [0:00:08.080 --> 0:00:09.120] Fascinating question.
# [0:00:09.520 --> 0:00:09.620] Yeah.
# [0:00:09.620 --> 0:00:22.740] Have you experimented with it at all? I have not, but someone, the gentleman who runs the JRE companion page made a rap with chat GPT.
# [0:00:23.420 --> 0:00:35.260] Like was it, was it if Kanye West wrote a rap for chat GPT? They put it on Instagram, but it's, it's like, it seems like a person saying it.
# [0:00:35.640 --> 0:00:39.780] Like you want to try it? No, we can try it.
# [0:00:39.980 --> 0:00:41.180] I mean, it takes a long time.
# [0:00:41.340 --> 0:00:44.020] He, his thing took like 48 minutes to do.
# [0:00:44.340 --> 0:00:46.700] Well, whatever you want to look up right now, we can do it.
# [0:00:46.700 --> 0:00:46.860] Yeah.""")
# # data = farm.analyze("""meow""")
# console.log(data)


out = """             Here's the response as a JSON array with the requested clips from the podcast transcript:
                                                                                                                                                                                      
           [                                                                                                                                                                          
             {                                                                                                                                                                        
               "start":"0:03:34.400",                                                                                                                                                 
               "end":"0:03:52.640",                                                                                                                                                   
               "summary":"When asked about strategies for workers whose jobs will be eliminated by AI, he notes things have changed from his initial predictions.",                   
               "reason":"Interesting reflection on how his views have changed over time"                                                                                              
             },                                                                                                                                                                       
             {                                                                                                                                                                        
               "start":"0:06:54.300",                                                                                                                                                 
               "end":"0:07:11.740",                                                                                                                                                   
               "summary":"He discusses the importance of people having agency, self-determination and ability to participate in shaping the future alongside technological            
           progress.",                                                                                                                                                                
               "reason":"Thoughtful perspective on human needs beyond just economic issues"                                                                                           
             },                                                                                                                                                                       
             {                                                                                                                                                                        
               "start":"0:08:00.960",                                                                                                                                                 
               "end":"0:08:06.400",                                                                                                                                                   
               "summary":"He envisions a future where people have ownership stakes and voting rights in AI systems to help shape their development and benefits.",                    
               "reason":"Innovative idea around distributing ownership of advanced technologies"                                                                                      
             }                                                                                                                                                                        
           ]"""

print('[' + out.split("[").pop().split("]")[0] + ']')
