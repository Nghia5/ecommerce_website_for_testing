import * as Yup from "yup";

const validation = Yup.object({
  email: Yup.string()
    .email("Định dạng phải có '@' trong chuỗi")
    .required("Bạn chưa nhập địa chỉ email"),
  password: Yup.string()
    .min(8, "Yêu cầu tối thiểu 8 ký tự") 
    .required("Bạn chưa nhập mật khẩu"),
});

export default validation;
