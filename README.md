
im playing with an idea to "store data on real objects". eg on mushrooms or "trees".  of course not actually store the data on it. my idea is to work always with images of these real life objects. and then we use that images to "encode data" like this: eg: a photo of a tree of specific kind.  the AI analyzes what type of object this is, and how many different characteristics there are. eg for a tree for example his rings. but not only the rings, but like the shape and "holes" of the rings as well or so. AI (eg LLM with photo capabilities)  identifies how many "variable" patterns it has, to determine how many different combinations could exist in similar trees. of course there will be a tolerance determined by the AI because somethings look different in each photo even when the same. so they are less "safe" to use as "key characteristic". but then basically the AI generates a "encoding format" based on that characteristics. so that now you define data, eg "goodbye world", and define that the identified pattern on the photo (whcih we can change of course), equal your information. and then  you get a "key" which is like the decryption key, that defines the matching of the characteristics with your information / bits. 
so now with this key, others could upload a photo of the same tree and "read" the message you encoded onto it.
and eg if there is "empty bits", because there is much more possible information to be stored onto that "characteristics" combination, others could store data into parts using the same key. 
and like if you are the first person to store something on a "pattern" (identified by AI, in the beginning probably not super accurate but enough to start), other people will be able to use the same "pattern" key, so now they can store also information and read information. 

eg like steganography / PUFs (physical-uncloneable functions)

could this even work?


Some ideas i have for some challenges:
* weather ,lighting conditions, angles... etc - later, when more advanced, we will have AI models that first "identify" a specific object. based on gps location, multiple fotos, lidar data etc, we find or create a virtual representation of that object for reusing. so maybe that works well enough to eg make sure to differentiate different trees or recognize the same even in different angle, conditions etc.
* each object gets like a global UUID then
* it doesnt have to be PERFECT anyway for the beginning. 
* it seems like almost like steganography, but just, we dont wanna encode data in the actual image file. rather into whatever we have as a result from the image file...

