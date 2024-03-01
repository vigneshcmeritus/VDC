print("Setting UP")
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
from utlis import *
from sklearn.model_selection import train_test_split


#### STEP 1
path = "C:\\Users\\robot\\OneDrive\\Documents\\VDCCourse\\myData1"

data = importDataInfo(path)

#### STEP 2
data = balanceData(data, display=True)

#### STEP 3
imagesPath, steerings = loadData(path, data)

#### STEP 4
xTrain, xVal, yTrain, yVal = train_test_split(
    imagesPath, steerings, test_size=0.2, random_state=5
)
print("Total Training Images: ", len(xTrain))
print("Total Validation Images: ", len(xVal))
# 
####STEP 5

####STEP 6

####STEP 7

####STEP 8
model = createModel()
model.summary()

#### STEP 9
history = model.fit(
    batchGen(xTrain, yTrain, 100, 1),
    steps_per_epoch=300,
    epochs=5,
    validation_data=batchGen(xVal, yVal, 100, 0),
    validation_steps=200,
)

#### STEP 10
model.save("model_new1.h5")
print("Model Saved")

plt.plot(history.history["loss"])
plt.plot(history.history["val_loss"])
plt.legend(["Training", "validation"])
plt.ylim([0, 1])
plt.title("Loss")
plt.xlabel("Epoch")
plt.show()