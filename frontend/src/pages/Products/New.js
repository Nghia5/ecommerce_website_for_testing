</Text>
)}
</FormControl>
<FormControl mt={4}>
{/* <FormControl mt={4}>
<FormLabel>Photos</FormLabel>
<FieldArray
  name="photos"
@@ -164,7 +164,63 @@ function NewProduct() {
    </div>
  )}
/>
</FormControl>
</FormControl> */}
<FormControl mt={4}>
  <FormLabel>Photos</FormLabel>
  <FieldArray
    name="photos"
    render={(arrayHelpers) => (
      <div>
        {values.photos && values.photos.map((photo, index) => (
          <div key={index}>
            <Input
              name={`photos.${index}`}
              value={photo}
              disabled={isSubmitting}
              onChange={handleChange}
              width="90%"
              isInvalid={touched.photos?.[index] && errors.photos?.[index]} // Kiểm tra lỗi cho từng ảnh
            />
            {touched.photos?.[index] && errors.photos?.[index] && (
              <Text mt={2} color="red.500">{errors.photos[index]}</Text>
            )}

            {/* Hiển thị ảnh nếu URL hợp lệ */}
            {photo && (
              <div>
                <img
                  src={photo}
                  alt={`photo-${index}`}
                  style={{ maxWidth: "100px", marginTop: "10px", borderRadius: "5px" }}
                />
              </div>
            )}

            <Button
              ml="4"
              type="button"
              colorScheme="red"
              onClick={() => arrayHelpers.remove(index)}
            >
              Remove
            </Button>
          </div>
        ))}
        <Button
          mt="5"
          onClick={() => arrayHelpers.push("")}
        >
          Add a Photo
        </Button>
      </div>
    )}
  />
  {/* Hiển thị thông báo lỗi nếu mảng photos trống */}
  {touched.photos && errors.photos && typeof errors.photos === 'string' && (
    <Text mt={2} color="red.500">{errors.photos}</Text>
  )}
</FormControl>

<Button
mt={4}
width="full"
type="submit"
isLoading={isSubmitting}
>
Add Product
</Button>
</form>
</Box>
</Box>
</>
)}
</Formik>
</Box>
</div>
);
}
export default NewProduct;