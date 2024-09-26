### **Class Diagram Schema:**

1. **Class: User**
   * **Attributes:**
     * userID: int
     * name: string
     * email: string
     * phoneNumber: string
     * userType: string (enum: Seller/Buyer)
     * password: string
   * **Methods:**
     * register(): void
     * login(): void
     * logout(): void

---

2. **Class: Seller (inherits from User)**
   * **Attributes:**
     * sellerID: int
     * farmName: string
     * location: string
     * productList: List`<Product>`
   * **Methods:**
     * createOffer(): void
     * manageProduct(): void
     * setPrice(): void

---

3. **Class: Buyer (inherits from User)**
   * **Attributes:**
     * buyerID: int
     * companyName: string
     * purchaseHistory: List`<Transaction>`
   * **Methods:**
     * createBid(): void
     * makePurchase(): void
     * viewProducts(): void

---

4. **Class: Product**
   * **Attributes:**
     * productID: int
     * name: string
     * category: string
     * quantity: int
     * price: float
     * qualityCheck: QualityCheck
     * logisticsDetails: Logistics
   * **Methods:**
     * updateQuantity(): void
     * addLogistics(): void
     * setQualityCheck(): void

---

5. **Class: Transaction**
   * **Attributes:**
     * transactionID: int
     * productID: int
     * buyerID: int
     * sellerID: int
     * amount: float
     * status: string (enum: Pending/Completed/Failed)
     * paymentDetails: Payment
   * **Methods:**
     * initiateTransaction(): void
     * confirmPayment(): void
     * updateStatus(): void

---

6. **Class: Logistics**
   * **Attributes:**
     * logisticsID: int
     * transportMode: string
     * deliveryStatus: string
     * shippingDetails: string
   * **Methods:**
     * trackShipment(): void
     * updateStatus(): void

---

7. **Class: Payment**
   * **Attributes:**
     * paymentID: int
     * transactionID: int
     * paymentMethod: string
     * amount: float
     * paymentStatus: string (enum: Paid/Refunded/Pending)
   * **Methods:**
     * processPayment(): void
     * refundPayment(): void

---

8. **Class: QualityCheck**
   * **Attributes:**
     * checkID: int
     * productID: int
     * result: string
     * inspectorDetails: string
   * **Methods:**
     * verifyQuality(): void
     * issueCertification(): void

---

### **Relationships:**

1. **User → Buyer/Seller:**
   * Inheritance relationship: A User can either be a Buyer or a Seller.
2. **Seller → Product:**
   * Composition: A Seller owns multiple Products.
3. **Buyer → Transaction:**
   * Aggregation: A Buyer can make many Transactions.
4. **Product → Transaction:**
   * Association: A Product is linked to a Transaction.
5. **Transaction → Payment:**
   * Aggregation: A Transaction has a Payment.
6. **Product → QualityCheck:**
   * Aggregation: A Product has one QualityCheck.
7. **Product → Logistics:**
   * Association: A Product has associated Logistics for delivery.
