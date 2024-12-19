</Text>
          <Box mt={4}>
            <Text fontSize={20}>email: {user.email}</Text>
            <Text fontSize={20}>role: {user.role}</Text>
            <Text fontSize={20}>Email: {user.email}</Text>
            <Text fontSize={20}>Role: {user.role}</Text>
          </Box>

          <br />
          <br />
          <Link to="/">
            <Button colorScheme="pink" variant="solid" onClick={handleLogout}>
              Logout
            </Button>
          </Link>
        </>
      )}
    </div>
  );
}
export default Profile;