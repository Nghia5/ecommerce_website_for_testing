import * as Yup from "yup";

const forgotPasswordValidation = Yup.object({
  email: Yup.string()
    .email("Định dạng phải có '@' trong chuỗi")
    .required("Bạn chưa nhập địa chỉ email"),
});

export default forgotPasswordValidation;
