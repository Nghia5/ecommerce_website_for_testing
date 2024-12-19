import "./App.css";
import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Signin from "./pages/Auth/Signin/index";
import Signup from "./pages/Auth/Signup/index";
import ForgotPassword from "./pages/Auth/Signin/ForgotPassword"; // Import ForgotPassword
import Products from "./pages/Products/index";
import ProductDetail from "./pages/ProductDetail/index";
import Basket from "./pages/Basket/index";
@@ -24,6 +25,7 @@ function App() {
          <Route path="/product/:product_id" element={<ProductDetail />} />
          <Route path="/signin" element={<Signin />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/forgot-password" element={<ForgotPassword />} /> {/* Thêm Forgot Password */}
          <Route path="/basket" element={<Basket />} />
          <Route path="/profile" element={<ProductedProfile />} />
          <Route path="/admin">
            <Route index element={<ProductedAdmin />} />
            <Route path="orders" element={<Orders />} />
            <Route path="products">
              <Route index element={<AdminProducts />} />
              <Route path=":product_id" element={<AdminProductDetail />} />
              <Route path="new" element={<NewProduct />} />
            </Route>
          </Route>
          <Route path="*" element={<Error404 />} />
        </Routes>
      </div>
    </>
  );
}





export default App;