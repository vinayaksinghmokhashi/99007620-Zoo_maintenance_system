## 5. Test Plan and Output

### 5.1 High level test plan
|Test ID|Description|Input|Expected output|Actual Output|
|-------|-----------|-----|---------------|-------------|
|HLTP_01|Updating animal’s details|Animal’s details|Animal’s details in a list|Updated list with animal’s details|
|HLTP_02|View animal’s details|Open animals list|Animal’s details in a list display|Updated list with animal’s details displays.|
|HLTP_03|Check for Animals presence|Animal’s name|Animal’s details in a list if animal exists in zoo or not found.|Animal’s details in a list if animal exists in zoo or not found.|
|HLTP_04|Search for animal|User types animals name|Found or Not found|Found or Not found|

### 5.2 LOW LEVEL TEST PLAN
|Test ID|Description|HLTP ID|Input|Expected output|Actual Output|Status|
|-------|-----------|-----|--|---------------|-------------|------|
|LLTP_01|Add animal’s details|HLTP_01|Animal’s details|Animal’s details in a list|Updated list with animal’s details|✔️|
|LLTP_02|Edit animal’s details|HLTP_01|Animal’s details to be edited|Updated list with animal’s details displays.|Updated list with animal’s details displays.|✔️|
|LLTP_03|Delete Animal details|HLTP_01|Animal’s details to be deleted|Updated list with animal’s details displays.|Updated list with animal’s details displays.|✔️|
|LLTP_04|Search for animal|HLTP_04|User types animals name|Search for an animal and display Found or Not found|Found or Not found|✔️|
|LLTP_05|Veiwing animal list|HLTP_02|Option for display feature|Animal list displays|Animal list displays|✔️|
|LLTP_06|Check animals presence|HLTP_03|Option for animal check feature and type animal's name|Search for an animal and display Found or Not found|Found or Not found|✔️|

























