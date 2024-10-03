import * as yup from "yup";

const validations = yup.object().shape({
  email: yup.string().email("Nhap Email hop le").required("Bat buoc"),
  password: yup
    .string()
    // .min(10, "Parolanız en az 10 karakter olmalıdır.")
    .required(),
});

export default validations;
