import QZmodel

model = QZmodel.QZModel()
model.load_data()
model.build()
model.train()
model.predict()
model.save()
model.load()